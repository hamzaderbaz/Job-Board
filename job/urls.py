from django.urls import include, path
from django.contrib import admin

from . import api, views
# from .views import JobListView, JobDetailView
# from .views import add_job, job_detail, job_list
# from .views import Joblist

app_name = 'job'

urlpatterns = [
    

    path('', views.job_list, name='job_list'),
    path('<str:slug>/', views.job_detail, name='job_detail'),

    # path('', JobListView.as_view(), name='job_list'),
    # path('<str:slug>/', JobDetailView.as_view(), name='job_detail'),
    path('', views.add_job, name='add-job'),

    # path('', job_list.as_view, name='Joblist'),
    # path('', Joblist.as_view, name='Joblist'),
    

    #api
    path('api/jobs', api.job_list_api, name='job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),
    

    #GenericViews: class based views 
    path('api/v2/jobs', api.JobListApi.as_view(), name='JobListApi'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name='JobDetail'),
]



