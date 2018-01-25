from django.contrib import admin
from .models import JobLog, JobSchedule

admin.site.register(JobLog)
admin.site.register(JobSchedule)
