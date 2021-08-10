from django import forms


from .models import Student
class StudentForm(forms.ModelForm):
    dob=forms.DateField(label="Date of Birth",widget=forms.SelectDateWidget(years=range(1900,2100)))

    class Meta:
        model=Student
        fields="__all__"

