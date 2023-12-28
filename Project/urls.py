"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os  # needed by code below
from django.contrib.staticfiles import storage
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


# from job import views
from accounts import views
import job


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('jobs/', include('job.urls', namespace='jobs')),
    path('contact-us/', include('contact.urls', namespace='contact')),



    # URL of registrations
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),



    # URL of accounts app
    path('profile/', views.profile, name='profile'),
    path('profile/edit-profile/', views.profile_edit, name='profile_edit'),



    # URL of jobs app
    path('add-job/', job.views.add_job, name='add_job'),







    # APIs URL
    path('api-auth/', include('rest_framework.urls')),


]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

