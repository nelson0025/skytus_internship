
from django.db import models

# Create your models here.

class cource (models.Model):
    name =models.CharField(max_length=65)

    def __str__(self):
        return self.name
    
class student (models.Model):
    name = models.CharField(max_length= 60)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    cource=models.ForeignKey(cource,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class book(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    price=models.IntegerField()

