from .models import Lecturer,Student,User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class StudentSignupForm(UserCreationForm):
    name=forms.CharField(required=True)
    email=forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def data_save(self, commit=True):
        user=super().save(commit=False)
        user.is_student=True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.save()
        student=Student.objects.create(user=user)
        student.save()
        return student


class LecturerSignupForm(UserCreationForm):
    name = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_lecturer=True
        # user.is_staff=True
        user.name=self.cleaned_data.get('name')
        user.designation=self.cleaned_data.get('designation')
        user.save()
        lecturer=Lecturer.objects.create(user=user)
        lecturer.save()
        return lecturer



class LecturerForm(forms.ModelForm):
    class Meta:
        model=Lecturer
        # fields=['clg_name','dep_name','bran_name','lect_name','lect_sal','subject','time_table']
        fields='__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields ='__all__'
        # fields=['clg_name','dep_name','bran_name','stu_name','subject','time_table','fee','result']

# class FeeForm(forms.ModelForm):
#     class Meta:
#         model=Fee
#         fields='__all__'