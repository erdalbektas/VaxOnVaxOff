from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime, timedelta, date
from collections import defaultdict
from .models import Project, Task, WorkSchedule
from .serializers import ProjectSerializer, TaskSerializer, WorkScheduleSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all().order_by('deadline', '-importance')

    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        task = self.get_object()
        task.completed = not task.completed
        task.completed_at = timezone.now() if task.completed else None
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)


class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer

    def get_queryset(self):
        return WorkSchedule.objects.all()[:1]


@api_view(['POST'])
def generate_calendar(request):
    tasks = Task.objects.filter(completed=False).order_by('deadline', '-importance')
    schedule = WorkSchedule.objects.first()
    
    if not schedule:
        schedule = WorkSchedule.objects.create(
            work_days=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
            work_start='09:00',
            work_end='17:00',
            overtime_enabled=False
        )
    
    if not tasks.exists():
        return Response({
            'calendar': [],
            'overtime_required': False,
            'message': 'No tasks to schedule'
        })
    
    work_days_set = set(schedule.work_days)
    
    work_start = datetime.strptime(str(schedule.work_start), '%H:%M:%S').time()
    work_end = datetime.strptime(str(schedule.work_end), '%H:%M:%S').time()
    
    lunch_start = None
    lunch_end = None
    if schedule.lunch_start and schedule.lunch_end:
        lunch_start = datetime.strptime(str(schedule.lunch_start), '%H:%M:%S').time()
        lunch_end = datetime.strptime(str(schedule.lunch_end), '%H:%M:%S').time()
    
    today = date.today()
    start_date = today
    
    calendar_days = defaultdict(list)
    total_hours_needed = 0
    total_hours_scheduled = 0
    overtime_hours = 0
    overtime_required = False
    
    importance_order = {'high': 0, 'medium': 1, 'low': 2}
    
    sorted_tasks = sorted(
        tasks, 
        key=lambda t: (t.deadline, importance_order.get(t.importance, 1))
    )
    
    day_offset = 0
    current_task_idx = 0
    
    while current_task_idx < len(sorted_tasks):
        current_date = start_date + timedelta(days=day_offset)
        day_name = current_date.strftime('%a')
        
        if day_name not in work_days_set:
            day_offset += 1
            continue
        
        day_start = datetime.combine(current_date, work_start)
        day_end = datetime.combine(current_date, work_end)
        
        available_minutes = (day_end - day_start).seconds // 60
        lunch_minutes = 0
        lunch_start_dt = None
        lunch_end_dt = None
        if lunch_start and lunch_end:
            lunch_start_dt = datetime.combine(current_date, lunch_start)
            lunch_end_dt = datetime.combine(current_date, lunch_end)
            lunch_minutes = (lunch_end_dt - lunch_start_dt).seconds // 60
            available_minutes -= lunch_minutes
        
        normal_available_minutes = available_minutes
        current_time = day_start
        day_has_overtime = False
        
        while current_task_idx < len(sorted_tasks):
            task = sorted_tasks[current_task_idx]
            task_hours = float(task.work_hours)
            task_minutes = int(task_hours * 60)
            total_hours_needed += task_hours
            
            if task.deadline < current_date:
                calendar_days[current_date].append({
                    'task': TaskSerializer(task).data,
                    'start_time': None,
                    'end_time': None,
                    'status': 'overdue',
                    'message': f'Deadline passed: {task.deadline}'
                })
                current_task_idx += 1
                continue
            
            if task_minutes > available_minutes and not schedule.overtime_enabled:
                overtime_required = True
                hours_needed = task_minutes - available_minutes
                overtime_hours += hours_needed / 60
                
                if available_minutes > 0:
                    calendar_days[current_date].append({
                        'task': TaskSerializer(task).data,
                        'start_time': current_time.strftime('%H:%M'),
                        'end_time': day_end.strftime('%H:%M'),
                        'status': 'partial',
                        'message': f'Partially scheduled. Need {hours_needed/60:.1f}h more'
                    })
                    total_hours_scheduled += available_minutes / 60
                    day_has_overtime = True
                break
            
            task_start = current_time.strftime('%H:%M')
            task_end_dt = current_time + timedelta(minutes=task_minutes)
            task_end = task_end_dt.strftime('%H:%M')
            
            if task_end_dt > day_end:
                overtime_required = True
                day_has_overtime = True
                actual_work_minutes = (day_end - current_time).seconds // 60
                overtime_hours += (task_minutes - actual_work_minutes) / 60
                total_hours_scheduled += actual_work_minutes / 60
            else:
                total_hours_scheduled += task_minutes / 60
                available_minutes -= task_minutes
            
            calendar_days[current_date].append({
                'task': TaskSerializer(task).data,
                'start_time': task_start,
                'end_time': task_end,
                'status': 'overtime' if task_end_dt > day_end else 'scheduled',
                'message': 'Scheduled with overtime' if task_end_dt > day_end else 'Successfully scheduled'
            })
            
            current_time = task_end_dt
            current_task_idx += 1
            
            if lunch_start_dt and lunch_end_dt and current_time <= lunch_start_dt:
                pass
            elif lunch_start_dt and lunch_end_dt and current_time > lunch_start_dt and current_time < lunch_end_dt:
                current_time = lunch_end_dt
                available_minutes -= lunch_minutes
        
        day_offset += 1
    
    calendar_result = []
    for day in sorted(calendar_days.keys()):
        day_tasks = calendar_days[day]
        day_total_hours = sum(
            (datetime.strptime(t['end_time'], '%H:%M') - datetime.strptime(t['start_time'], '%H:%M')).seconds / 60 / 60
            for t in day_tasks if t['start_time'] and t['end_time']
        )
        
        calendar_result.append({
            'date': day.isoformat(),
            'day_name': day.strftime('%A'),
            'tasks': day_tasks,
            'total_hours': round(day_total_hours, 1)
        })
    
    return Response({
        'calendar': calendar_result,
        'overtime_required': overtime_required,
        'overtime_hours': round(overtime_hours, 1),
        'total_hours_scheduled': round(total_hours_scheduled, 1),
        'total_hours_needed': round(total_hours_needed, 1)
    })
