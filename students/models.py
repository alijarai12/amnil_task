from django.db import models

# Create your models here.
class Student(models.Model):
    fulname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    