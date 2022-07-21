from django.contrib import admin

# Register your models here.

from .models import Job, category   # عملنا  . علشان همل الاتنين في نفس الفولدر 

admin.site.register(Job) #  اي كلاس تعملة في الموديل تيجي تضيفه في الادمن
admin.site.register(category) #  
