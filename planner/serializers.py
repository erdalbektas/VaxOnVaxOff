from rest_framework import serializers
from .models import Project, Task, WorkSchedule


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'project', 'project_name', 'name', 'deadline', 'importance', 'work_hours', 'completed', 'completed_at', 'created_at']
        read_only_fields = ['id', 'created_at', 'completed_at']


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = ['id', 'work_days', 'work_start', 'work_end', 'lunch_start', 'lunch_end', 'overtime_enabled', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
