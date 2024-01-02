from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify



# Choices for job types: Full Time or Part Time
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time ', 'Part Time'),
)

# Function to handle image upload and naming
def image_upload(instance, filename):
    imagename, extention = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extention)



class Job(models.Model):  
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)  
    job_type = models.CharField(max_length=15, choices=JOB_TYPE) 
    description = models.TextField(max_length=10000) 
    published_at = models.DateTimeField(auto_now=False) 
    vacancy = models.IntegerField(default=1) 
    salary = models.IntegerField(default=0) 
    category = models.ForeignKey('category', on_delete=models.CASCADE) 
    experience = models.IntegerField(default=1) 
    image = models.ImageField(upload_to=image_upload) 
    slug = models.SlugField(blank=True, null=True) 


    # Override save method to automatically generate slug from title
        
    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        super(Job, self).save(*args, **kwargs)  

    def __str__(self):
        return self.title  



class category(models.Model):
    name = models.CharField(max_length=25) 

    def __str__(self):
        return self.name   



class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE) 
    name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=100) 
    website = models.URLField() 
    CV = models.FileField(upload_to='apply/') 
    cover_letter = models.TextField(max_length=500) 
    created_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name  
