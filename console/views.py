from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import JobLog, JobSchedule


def index(request):
    context = {}
    return render(request, 'console/index.html', context)


def jobLog(request):
    jobList = JobLog.objects.order_by('-job_id')
    context = {
        'jobList': jobList
    }
    return render(request, 'console/joblog.html', context)


def jobSchedule(request, job_id):

    jobLog = get_object_or_404(JobLog, pk=job_id)
    jobSchedule = get_list_or_404(JobSchedule.objects.order_by('-sequence'),
                                  job_id=job_id)

    context = {
        'jobLog': jobLog,
        'jobSchedule': jobSchedule
    }

    return render(request, 'console/jobschedule.html', context)
