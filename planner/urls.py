from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'schedule', views.WorkScheduleViewSet, basename='schedule')

urlpatterns = [
    path('', include(router.urls)),
    path('generate-calendar/', views.generate_calendar, name='generate-calendar'),
]
