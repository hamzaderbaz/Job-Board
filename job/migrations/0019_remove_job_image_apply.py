# Generated by Django 4.0.4 on 2022-08-19 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_job_slug_alter_job_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('cover_letter', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.job')),
            ],
        ),
    ]
