from django.contrib import admin

from .models import (Apply, Job, category) # we make (.) behind, Because they are all in the same folder



admin.site.register(Job) #  Any class you make in the model, you will add it in the admin
admin.site.register(category) 
admin.site.register(Apply) 


