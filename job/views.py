from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse

from .filters import JobFilter
from .form import ApplyForm, JobForm
from .models import Job

# Create your views here.


def job_list(request):

    job_list = Job.objects.all()  # نرجع كل الوظائف# Show 25 contacts per page عدد الصفحات اللي بتتعامل معاه
    
    #Filters
    myfilters =  JobFilter(request.GET, queryset=job_list)
    job_list = myfilters.qs 
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj, 'myfilters': myfilters}  # template name
    return render(request,'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)  # نرجع وظيفة واحدة
    
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            print('done')
    else:
        form = ApplyForm()

    # job cause we search on just one job
    context = {'job': job_detail, 'form':form}
    return render(request,'job/job_detail.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()

    return render(request,'job/add_job.html', {'form': form})



