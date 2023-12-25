from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer


# API view function to list all jobs
@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()  # Fetch all jobs from the database
    data = JobSerializer(all_jobs, many=True).data  # Serialize job data
    return Response({'data': data})  # Return serialized data in a response


# API view function to retrieve details of a specific job
@api_view(['GET'])
def job_detail_api(request, id):
    job_detail = Job.objects.get(id=id)  # Fetch a specific job based on ID
    data = JobSerializer(job_detail).data  # Serialize job detail data
    return Response({'data': data})  # Return serialized data in a response


# Using generic views for handling API functionality (List and Create)
class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()  # Queryset for JobListApi view
    serializer_class = JobSerializer  # Serializer class for JobListApi view


# Using generic views for handling API functionality (Retrieve, Update, Destroy)
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()  # Queryset for JobDetail view
    serializer_class = JobSerializer  # Serializer class for JobDetail view
    lookup_field = 'id'  # Field used for looking up specific job details


# Viewsets are used to define API endpoints for CRUD operations
# They typically bundle the model and URL configurations together
# (Not explicitly provided in the code snippet)
