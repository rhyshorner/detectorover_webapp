# Generated by Django 3.1.7 on 2021-05-21 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_url',
        ),
    ]
