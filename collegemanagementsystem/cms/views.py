from django.shortcuts import render,redirect
from .models import Lecturer,Student
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import LecturerForm,StudentForm



@login_required(login_url='login')
def showindex(request):
    if request.user.is_authenticated:
        user=request.user
        return render(request,'index.html')


def login(request):
    if request.method=='GET':
    #     un=request.POST.get('username')
    #     pw1=request.POST.get('password1')
    #     pw2=request.POST.get('password2')
    #     type=request.POST.get('regi')
    #     print(type)
    #     form1=AuthenticationForm(username=un,password=pw1,password2=pw2)
        form1=AuthenticationForm()
        return render(request,'login.html',{'form':form1})
    else:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            type=request.POST.get('regi')
            print(username)
            print(password)
            print(type)
            if type == 'Lecturer':
                print('-----------')

                user=authenticate(username=username,password=password)
                print('------')
                if user is not None:
                    loginUser(request, user)
                    return redirect('addlect')
                else:
                    return render(request, 'login.html', {'form': form})



            elif type == 'Student':
                user = authenticate(username=username, password=password)
                if user is not None:
                    loginUser(request, user)
                    return redirect('addstud')
                else:
                    return render(request, 'login.html', {'form': form})
            # elif type == 'staff':
            #     user=authenticate(username=username,password=password)
            #     if user is not None:
            #         loginUser(request, user)
            #         return redirect('main')
            #     else:
            #         return render(request, 'login.html', {'form': form})
            else:
                return redirect('login')


                # return redirect('student')




def signup(request):
    if request.method=='POST':
        form=UserCreationForm()
        return render(request,'signup.html',{'form':form})
    else:
        print(request.POST)
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request,'signup.html',{'form':form})



def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def addlect(request):
    if request.user.is_authenticated:
        user=request.user
        print(user)
        lf=LecturerForm(request.POST)
        if lf.is_valid():
            print(lf.cleaned_data)
            Lecturer=lf.save(commit=False)
            Lecturer.user=user
            Lecturer.save()
            print(Lecturer)
            return redirect('addlect')
        else:
            return render(request,'addlect.html',context={'form':lf})

def lecturer(request):
    lect = Lecturer.objects.all()
    context={'lect':lect}
    return render(request, 'lecturer.html', context)

def deletelect(request,id):
    print(id)
    Lecturer.objects.get(pk=id).delete()
    return redirect('lecturer')

@login_required(login_url='login')
def addstud(request):
    if request.user.is_authenticated:
        user=request.user
        print(user)
        sf=StudentForm(request.POST)
        if sf.is_valid():
            Student=sf.save(commit=False)
            Student.user=user
            Student.save()
            print(Student)
            return redirect('student')
        else:
            return render(request,'addstu.html',context={'form':sf})

def student(request):
    stu=Student.objects.all()
    context={'stu':stu}
    return render(request,'student.html',context)


def deletestud(request,id):
    print(id)
    Student.objects.get(pk=id).delete()
    return redirect('student')
