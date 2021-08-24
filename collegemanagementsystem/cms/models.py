from django.db import models
from django.contrib.auth.models import AbstractBaseUser



# class User(AbstractBaseUser):
#     is_student=models.BooleanField(default=False)
#     is_lecturer=models.BooleanField(default=False)



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
    # id = models.IntegerField(primary_key=True)
    # clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    # dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    # bran_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date=models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()


    def __str__(self):
        return f''

class Salary(models.Model):
    salary = models.FloatField(max_length=30)

    def __str__(self):
        return str(self.salary)


class Fee(models.Model):
    coll_fee=models.IntegerField()
    exam_fee=models.IntegerField()

    def __str__(self):
        return f'{self.coll_fee}{self.exam_fee}'


class Subject(models.Model):
    # clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    # dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    # stu_name = models.OneToOneField(Student, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=20)
    # time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    # fee=models.ForeignKey(Fee,on_delete=models.CASCADE)

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
    # clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    # dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    # stu_name = models.OneToOneField(Student, on_delete=models.CASCADE)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    result = models.CharField(max_length=12,choices=results_choices)

    def __str__(self):
        return str(self.result)


class Student(models.Model):
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    bran_name=models.ForeignKey(Branch,on_delete=models.CASCADE)
    stu_name = models.CharField(max_length=20)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee,on_delete=models.CASCADE)
    result=models.ForeignKey(Results,on_delete=models.CASCADE)


    def __str__(self):
        return self.stu_name



class Staff(models.Model):
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    staff_salary = models.OneToOneField(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    bran_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    lect_name = models.CharField(max_length=20)
    lect_sal=models.ForeignKey(Salary,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)

    def __str__(self):
        return self.lect_name




# class Exams(models.Model):
#     clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
#     dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
#     stu_name = models.OneToOneField(Student, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
#

# class TimeTable(models.Model):
#     id = models.IntegerField(primary_key=True)
#     clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
#     dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
#     bran_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     time_start = models.TimeField()
#     time_end = models.TimeField()


# results_choices = [
#     ('Above 90.00'  'Grade A'),
#     ('81.00 - 90.00' 'Grade B2'),
#     ('61.00 - 80.00'  'Grade C1'),
#     ('41.00 - 60.00'  'Grade C2'),
#     ('35.00 - 40.00'  'Grade D'),
#     ('21 - 35'  'E1'),
#     ('Below 21 - E2'  'Needs Improvement'),
# ]



# class Fee(models.Model):
#     clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
#     dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
#     stu_name = models.OneToOneField(Student, on_delete=models.CASCADE)
#     fee = models.IntegerField(max_length=20)
#
#
# class CollegeFee(models.Model):
#     clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
#     dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
#     stu_name = models.OneToOneField(Student, on_delete=models.CASCADE)
#     fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
#
#
# class ExamFee(models.Model):
#     clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
#     dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
#     stu_name = models.OneToOneField(Student, on_delete=models.CASCADE)
#     fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
#