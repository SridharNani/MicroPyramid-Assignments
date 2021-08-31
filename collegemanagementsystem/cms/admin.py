from django.contrib import admin
from .models import College,Depart,Branch,TimeTable,Salary,Student,Subject,Staff,Lecturer,Results,User
# Register your models here.
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(College)
admin.site.register(Subject)
admin.site.register(Salary)
admin.site.register(Branch)
admin.site.register(Staff)
admin.site.register(Depart)
admin.site.register(TimeTable)
# admin.site.register(Fee)
admin.site.register(Results)


# admin.site.register(Results)
# admin.site.register(Results)
admin.site.register(User)
