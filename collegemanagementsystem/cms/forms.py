from .models import Lecturer,Student
from django import forms
from django.core import validators



class LecturerForm(forms.ModelForm):
    class Meta:
        model=Lecturer
        fields=['clg_name','dep_name','bran_name','lect_name','lect_sal','subject','time_table']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['clg_name','dep_name','bran_name','stu_name','subject','time_table','fee','result']