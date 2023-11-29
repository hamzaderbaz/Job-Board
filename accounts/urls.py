from django.urls import include, path
from django.contrib import admin

from . import views
from .views import logout, signup

app_name = 'accounts'


urlpatterns = [

    path('login/', views.login, name='login'),
    path('signup/', signup, name='signup'),
    path('', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('logout/', logout, name='logout'),


]
