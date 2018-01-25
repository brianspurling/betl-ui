from django.urls import path

from . import views

app_name = 'console'
urlpatterns = [
    path('', views.index, name='index'),
    path('logs/', views.jobLog, name='jobLog'),
    path('logs/<int:job_id>/', views.jobSchedule, name='jobSchedule'),
]
