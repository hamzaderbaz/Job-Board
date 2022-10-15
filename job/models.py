from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.


''' 
django model field :
-html widget     ديجانجو هيديلك ليه شكل في ال html    
-validation  زي انك لما تدخل اميل ساعتها ديجانجو يتأكد لو دا اميل ولا لا 
-db size

'''

JOB_TYPE = (

    ('Full Time', 'Full Time'),
    ('Part Time ', 'Part Time'),
)


def image_upload(instance, filename):
    imagename, extention = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extention)


class Job(models.Model):  # class equal thing in DB is table   # انشأنا  جدول في الداتابيز اسمه Job
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE) # column   # وانشأنا تحته عمود اسمه titl
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE) #job_type is Full Time or Part Time
    description = models.TextField(max_length=10000) #use textfield cause 1000 lenght (more words used)
    published_at = models.DateTimeField(auto_now=False) #use datefield cause published at some date
    vacancy = models.IntegerField(default=1) #IntegerField اي حاجة بارقام نستخدم ال
    salary = models.IntegerField(default=0) #دي بتعني عدد البوزيشنس المتاحة
    # job be in one category but category be in many jobs (one to many)
    category = models.ForeignKey('category', on_delete=models.CASCADE) # 'category' with single cote cause class category came after and python work step by step
    # الديفولت اللي هو شي الافتراضي
    experience = models.IntegerField(default=1)# لما يكون 0 نسيب اليوزر يفرض المرتب اللي هو عاوزه انما ال 1 انت اللي بتفرض الرقم زي انك عاوز موظف خبرة 5 سنين
    image = models.ImageField(upload_to = image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.title  # هنا رجع التايتيل علشان يعرف يسمي اسم الوظيفة زي ما هو عاوز


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
