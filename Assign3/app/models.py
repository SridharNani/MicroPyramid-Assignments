from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30,unique=True)
    age = models.IntegerField()
    contact=models.CharField(max_length=12)
    email=models.EmailField(max_length=30)
    image = models.ImageField(upload_to="product_images/")

