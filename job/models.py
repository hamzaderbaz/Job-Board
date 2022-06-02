from django.db import models

# Create your models here.


''' 
django model field :
-html widget
-validation 
-db size

'''

JOB_TYPE = (

    ('Full Time','Full Time'),
    ('Part Time ','Part Time'),
)



class Job(models.Model):      #class equal thing in DB is table   # انشأنا  جدول في الداتابيز اسمه Job  
    title = models.CharField(max_length = 100)     #column   # وانشأنا تحته عمود اسمه titl  
    #location
    job_type = models.CharField(max_length = 15, choices= JOB_TYPE)
    description = models.TextField(max_length = 1000 )
    published_at = models.DateTimeField(auto_now = False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title





