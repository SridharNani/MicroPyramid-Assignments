from django.db import models

# Create your models here.
sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class College(models.Model):
    coll_name=models.CharField(primary_key=True,unique=True,max_length=100)

    def __str__(self):
        return self.coll_name

class Dept(models.Model):
    d_id=models.IntegerField(primary_key=True)
    clg=models.ForeignKey(College,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)


    def __str__(self):
        return self.name



class Lecturer(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    clg=models.ForeignKey(College,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    dep=models.ManyToManyField(Dept)

    def __str__(self):
        return self.name


class Student(models.Model):
    rolln=models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=100,unique=True)
    gender = models.CharField(max_length=50, choices=sex_choice)
    lec_name=models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    clg=models.ForeignKey(College,on_delete=models.CASCADE)
    dep = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

