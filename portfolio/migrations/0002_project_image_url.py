# Generated by Django 3.1.7 on 2021-05-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_url',
            field=models.URLField(max_length=400, null=True),
        ),
    ]