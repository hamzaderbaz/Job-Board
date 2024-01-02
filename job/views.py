from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Job
from .form import ApplyForm, JobForm
from .filters import JobFilter
from django_filters.views import FilterView




# class job_list(FilterView):
#     model = Job
#     paginate_by = 3
#     filterset_class = JobFilter
#     template_name = 'job/job_list.html'



# View function to display a list of jobs with pagination and filtering
def job_list(request):
    job_list = Job.objects.all()  
    myfilters = JobFilter(request.GET, queryset=job_list)
    job_list = myfilters.qs 
    paginator = Paginator(job_list, 4)  # Show 3 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj, 'filter': myfilters}  # Prepare context for the template
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



# from pyexpat.errors import messages
# from django.contrib.auth.decorators import login_required
# # from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import redirect, render, get_object_or_404
# from django.urls import reverse
# from django.views import View
# from .models import Job
# from .form import ApplyForm, JobForm
# from .filters import JobFilter
# from django_filters.views import FilterView




# class JobListView(FilterView):
    
#     model = Job
#     paginate_by = 4
#     filterset_class = JobFilter
#     template_name = 'job/job_list.html'
#     context_object_name = 'jobs'
    

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     queryset = context[self.context_object_name]
#     #     paginator = Paginator(queryset, self.paginate_by)

#     #     page = self.request.GET.get('page')
#     #     try:
#     #         jobs = paginator.page(page)
#     #     except PageNotAnInteger:
#     #         jobs = paginator.page(1)
#     #     except EmptyPage:
#     #         jobs = paginator.page(paginator.num_pages)

#     #     context['jobs'] = jobs
#     #     return context


# class JobDetailView(View):
#     template_name = 'job/job_detail.html'

#     def get(self, request, slug):
#         job = get_object_or_404(Job, slug=slug)
#         form = ApplyForm()
#         context = {'job': job, 'form': form}
#         return render(request, self.template_name, context)

#     def post(self, request, slug):
#         job = get_object_or_404(Job, slug=slug)
#         form = ApplyForm(request.POST, request.FILES)

#         if form.is_valid():
#             myform = form.save(commit=False)
#             myform.job = job
#             myform.save()
#             print('done')

#         context = {'job': job, 'form': form}
#         return render(request, self.template_name, context)

# @login_required
# def add_job(request):
#     if request.method == 'POST':
#         form = JobForm(request.POST, request.FILES)
#         if form.is_valid():
#             myform = form.save(commit=False)
#             myform.owner = request.user
#             myform.save()
#             return redirect(reverse('jobs:job_list'))  # Redirect to the job list page after successful addition
#     else:
#         form = JobForm()

#     return render(request, 'job/add_job.html', {'form': form})  # Prepare context for the template


# @login_required
# def add_job(request, job_id):
#     job = get_object_or_404(Job, id=job_id)
    
#     if request.method == 'POST':
#         if request.user.is_authenticated:  # Check if the user is authenticated
#             form = ApplyForm(request.POST, request.FILES)
#             if form.is_valid():
#                 application = form.save(commit=False)
#                 application.job = job
#                 application.save()
#                 messages.success(request, 'You have successfully applied for the job.')
#                 return redirect(reverse('jobs:job_detail', kwargs={'slug': job.slug}))
#         else:
#             messages.info(request, 'Please log in to apply for the job.')
#             return redirect(reverse('accounts:login'))  # Redirect to the login page

#     else:
#         form = ApplyForm()

#     return render(request, 'job/apply_job.html', {'form': form, 'job': job})



