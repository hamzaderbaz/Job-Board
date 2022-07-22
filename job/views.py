from django.shortcuts import render
from .models import Job
# Create your views here.

def job_list(request):
    job_list = Job.objects.all() # نرجع كل الوظائف 
    context = {'jobs': job_list} #template name
    return render(request,'job/job_list.html', context)

def job_detail(request, id):
    job_detail = Job.objects.get(id=id) # نرجع وظيفة واحدة
    context = {'job': job_detail} #job cause we search on just one job 
    return render(request,'job/job_detail.html', context)



