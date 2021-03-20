from django.db import models

# Create your models here.
class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    manufacturer = models.CharField(max_length=50)
    manufacturer_part_number = models.CharField(max_length=50)
    supplier = models.CharField(max_length=50)
    supplier_part_number = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits = 8, decimal_places = 2)
    
    def __str__(self):
        return 'name: {}'.format(self.title)