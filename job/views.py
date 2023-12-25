from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from .filters import JobFilter
from .form import ApplyForm, JobForm
from .models import Job



# View function to display a list of jobs with pagination and filtering
def job_list(request):
    job_list = Job.objects.all()  # Retrieve all available jobs

    # Apply filters based on user input
    myfilters = JobFilter(request.GET, queryset=job_list)
    job_list = myfilters.qs 
    paginator = Paginator(job_list, 3)  # Show 3 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj, 'myfilters': myfilters}  # Prepare context for the template
    return render(request, 'job/job_list.html', context)


# View function to display details of a specific job
def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)  # Retrieve a single job
    
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            print('done')
    else:
        form = ApplyForm()

    context = {'job': job_detail, 'form': form}  # Prepare context for the template
    return render(request, 'job/job_detail.html', context)


# View function to add a new job (requires user authentication)
@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))  # Redirect to the job list page after successful addition
    else:
        form = JobForm()

    return render(request, 'job/add_job.html', {'form': form})  # Prepare context for the template
