from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Importance(models.TextChoices):
        HIGH = 'high', 'High'
        MEDIUM = 'medium', 'Medium'
        LOW = 'low', 'Low'

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    deadline = models.DateField()
    importance = models.CharField(max_length=10, choices=Importance.choices, default=Importance.MEDIUM)
    work_hours = models.DecimalField(max_digits=4, decimal_places=1)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.name}"

    class Meta:
        ordering = ['deadline', '-importance']


class WorkSchedule(models.Model):
    work_days = models.JSONField(default=list)
    work_start = models.TimeField(default='09:00')
    work_end = models.TimeField(default='17:00')
    lunch_start = models.TimeField(null=True, blank=True)
    lunch_end = models.TimeField(null=True, blank=True)
    overtime_enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Work Schedule: {self.work_days}"

    class Meta:
        ordering = ['-created_at']
