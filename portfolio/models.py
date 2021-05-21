from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    programming_language = models.CharField(max_length=50)
    #image_url = models.URLField(max_length=400, null=True)

    def __str__(self):
        return 'title: {}'.format(self.title)