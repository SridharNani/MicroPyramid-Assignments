from django.shortcuts import render

# Create your views here.
from .models import Student,College,Lecturer,Dept



def student(request):
    if request.method=='POST':
        stuname=request.POST.get('s1')

        stmodel=Student.objects.filter(name__contains=stuname)
        return render(request,'student.html',{'sm':stmodel})
    else:
        return render(request,'student.html')

def lecturer(request):
    if request.method=='POST':
        lect=request.POST.get('s2')
        print(lect)

        lm=Lecturer.objects.filter(name__contains=lect)
        print(lm.values())

        dep=Dept.objects.filter(lecturer__name__contains=lect)
        print(dep.values())
        return render(request,'lecturer.html',{'res':lm,'dm':dep})
    else:
        return render(request,'lecturer.html')


def department(request):
    if request.method=='POST':
        dname=request.POST.get('s3')
        print(dname)
        sm=Student.objects.filter(dep=Dept.objects.get(name=dname))
        print('student')
        print(sm.values())
        lm=Lecturer.objects.filter(dep=Dept.objects.get(name=dname))
        print('lecturer')
        print(lm.values())

        return render(request,'department.html',{'sm':sm,'lm':lm})

    else:
        return render(request,'department.html')



