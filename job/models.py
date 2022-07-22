from django.db import models

# Create your models here.


''' 
django model field :
-html widget     ديجانجو هيديلك ليه شكل في ال html    
-validation  زي انك لما تدخل اميل ساعتها ديجانجو يتأكد لو دا اميل ولا لا 
-db size

'''

JOB_TYPE = (

    ('Full Time','Full Time'),
    ('Part Time ','Part Time'),
)

def image_upload(instance, filename):
    imagename, extention = filename.split(".")
    return "jobs/%s.%s"%(instance.id, extention)


class Job(models.Model):      #class equal thing in DB is table   # انشأنا  جدول في الداتابيز اسمه Job  
    title = models.CharField(max_length = 100)     #column   # وانشأنا تحته عمود اسمه titl  
    #location = 
    job_type = models.CharField(max_length = 15, choices= JOB_TYPE) #job_type is Full Time or Part Time
    description = models.TextField(max_length = 1000 ) #use textfield cause 1000 lenght (more words used) 
    published_at = models.DateTimeField(auto_now = False) #use datefield cause published at some date 
    vacancy = models.IntegerField(default=1) # دي بتعني عدد البوزيشنس المتاحة 
    salary = models.IntegerField(default=0) # IntegerField اي حاجة بارقام نستخدم ال 
    category = models.ForeignKey('category', on_delete = models.CASCADE) #job be in one category but category be in many jobs (one to many)
    #'category' with single cote cause class category came after and python work step by step
    experience = models.IntegerField(default=1) # الديفولت اللي هو شي الافتراضي 
    #لما يكون 0 نسيب اليوزر يفرض المرتب اللي هو عاوزه انما ال 1 انت اللي بتفرض الرقم زي انك عاوز موظف خبرة 5 سنين
    
    image = models.ImageField(upload_to = image_upload)
    
    def __str__(self):
        return self.title # هنا رجع التايتيل علشان يعرف يسمي اسم الوظيفة زي ما هو عاوز 


class category(models.Model):
    name =  models.CharField(max_length = 25)
    
    def __str__(self):
        return self.name


