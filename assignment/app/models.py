from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,blank=True,unique=True)
    pno=models.CharField(max_length=10,blank=True)
    age=models.IntegerField(blank=True,null=True)
    dob=models.DateField()



