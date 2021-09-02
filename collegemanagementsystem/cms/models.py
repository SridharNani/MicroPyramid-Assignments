from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_lecturer=models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # is_admin=models.BooleanField(default=False)


class College(models.Model):
    clg_name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.clg_name


class Depart(models.Model):
    id = models.IntegerField(primary_key=True)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=20)

    def __str__(self):
        return self.dep_name


class Branch(models.Model):
    id = models.IntegerField(primary_key=True)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    bran_name = models.CharField(max_length=20)

    def __str__(self):
        return self.bran_name

class TimeTable(models.Model):
    date=models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()


    def __str__(self):
        return f''

class Salary(models.Model):
    salary = models.FloatField(max_length=30)

    def __str__(self):
        return str(self.salary)


# class Fee(models.Model):
#     coll_fee=models.IntegerField()
#     exam_fee=models.IntegerField()
#
#     def __str__(self):
#         return f'{self.coll_fee}{self.exam_fee}'


class Subject(models.Model):
    sub_name = models.CharField(max_length=20)

    def __str__(self):
       return self.sub_name

results_choices=(
    ("First class", "Grade A"),
    ("second class","Grade B2"),
    ("Third class","Grade C1"),
    ("fourth class","Grade C2"),
    ("Destiniction","Grade D1"),
)

class Results(models.Model):
    result = models.CharField(max_length=12,choices=results_choices)

    def __str__(self):
        return str(self.result)


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    bran_name=models.ForeignKey(Branch,on_delete=models.CASCADE)
    stu_name = models.CharField(max_length=20)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    coll_fee = models.IntegerField()
    exam_fee = models.IntegerField()
    result=models.ForeignKey(Results,on_delete=models.CASCADE)


    def __str__(self):
        return self.stu_name

role_choice=(
    ('Puene','Puene'),
    ('Attender','Attender'),
    ('Swepaer','Sweaper'),
    ('Watchman','Watchman'),
)

class Staff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    staff_role=models.CharField(max_length=20,choices=role_choice)
    staff_salary = models.OneToOneField(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)


    # student=models.ForeignKey(Student,on_delete=models.CASCADE)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    bran_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    lect_name = models.CharField(max_length=20)
    lect_sal=models.ForeignKey(Salary,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)

    def __str__(self):
        return self.lect_name



