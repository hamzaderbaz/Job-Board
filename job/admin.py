from django.contrib import admin

from .models import (Apply, Job,  # عملنا  . علشان همل الاتنين في نفس الفولدر
                     category)

# Register your models here.


admin.site.register(Job) #  اي كلاس تعملة في الموديل تيجي تضيفه في الادمن
admin.site.register(category) #  
admin.site.register(Apply) 


