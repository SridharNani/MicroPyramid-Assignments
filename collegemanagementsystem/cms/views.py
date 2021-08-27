from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Lecturer,Student,User
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import StudentSignupForm,LecturerForm,StudentForm,LecturerSignupForm
from django.views.generic import CreateView


# @login_required(login_url='login')
def showindex(request):
    # if request.user.is_authenticated:
    #     user=request.user
        return render(request,'index.html')

class studentsignup(CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = 'studsignup.html'


    def form_valid(self, form):
        user=form.save()
        login(self.request)
        return redirect('login')

class lectsignup(CreateView):
    model = User
    form_class = LecturerSignupForm
    template_name = 'lectsignup.html'

    def form_valid(self, form):
        user=form.save()
        login(self.request, )
        return redirect('login')


def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                loginUser(request,user)
                return redirect('main')
            else:
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid Username or password')

    return render(request,'login.html',{'form':AuthenticationForm()})




# def lectsignup(request):
#     if request.method=='GET':
#         form=UserCreationForm()
#         return render(request,'lectsignup.html',{'form':form})
#     else:
#         print(request.POST)
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             print(user)
#             if user is not None:
#                 return redirect('login')
#         else:
#             return render(request,'lectsignup.html',{'form':form})
# def studsignup(request):
#     if request.method=='GET':
#         form=UserCreationForm()
#         return render(request,'studsignup.html',{'form':form})
#     else:
#         print(request.POST)
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             print(user)
#             if user is not None:
#                 return redirect('login')
#         else:
#             return render(request,'studsignup.html',{'form':form})



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

# @login_required(login_url='login')
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
