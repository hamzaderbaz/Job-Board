from django.urls import include, path
from django.contrib import admin

from . import views

app_name = 'accounts'


urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    #path('login', views.Login.as_view(), name='login'),

 
]
