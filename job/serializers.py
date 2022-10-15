# get data from models --> json
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'