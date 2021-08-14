from django.contrib import admin

# Register your models here.
from .models import Student,Lecturer,College,Dept

admin.site.register(Student)
admin.site.register(College)
admin.site.register(Lecturer)
admin.site.register(Dept)