# Generated by Django 4.0.4 on 2022-08-19 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0019_remove_job_image_apply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='job',
        ),
    ]
