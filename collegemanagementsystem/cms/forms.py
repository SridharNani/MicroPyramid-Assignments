from .models import Lecturer, Student, User, Staff, College,Depart,Branch,Subject,Salary,Results,TimeTable
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class StudentSignupForm(UserCreationForm):
    name = forms.CharField(required=True)
    # email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.name = self.cleaned_data.get('name')
        # user.email = self.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return student


class LecturerSignupForm(UserCreationForm):
    name = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_lecturer = True
        user.name = self.cleaned_data.get('name')
        user.designation = self.cleaned_data.get('designation')
        user.save()
        lecturer = Lecturer.objects.create(user=user)
        lecturer.save()
        return lecturer


class StaffSignupForm(UserCreationForm):
    # name = forms.CharField(required=True)
    role = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        # user.name = self.cleaned_data.get('name')
        user.role = self.cleaned_data.get('role')
        user.save()
        staff = Staff.objects.create(user=user)
        staff.save()
        return staff


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields=['clg_name','dep_name','bran_name','lect_name','lect_sal','subject','time_table']
        # fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields=['clg_name','dep_name','bran_name','stu_name','subject','time_table','coll_fee','exam_fee','result']


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        # fields = '__all__'
        fields = ['clg_name', 'name','staff_role','staff_salary']

class collegeForm(forms.ModelForm):
    class Meta:
        model=College
        fields='__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Depart
        fields='__all__'


class branchForm(forms.ModelForm):
    class Meta:
        model=Branch
        fields='__all__'

class subjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields='__all__'

class salaryForm(forms.ModelForm):
    class Meta:
        model=Salary
        fields='__all__'

class ResultForm(forms.ModelForm):
    class Meta:
        model=Results
        fields='__all__'

class TimetableForm(forms.ModelForm):
    class Meta:
        model=TimeTable
        fields='__all__'