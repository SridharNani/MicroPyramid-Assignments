from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Lecturer,Student,User
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import StudentSignupForm,LecturerForm,StudentForm,LecturerSignupForm,FeeForm
from django.views.generic import CreateView


# @login_required(login_url='login')
def showindex(request):
    # if request.method =='POST':
        if request.user.is_authenticated:
            user=request.user
            # if user.is_lecturer:
            #     return render(request,'index.html',{'l_user':user})
            # elif user.is_student:
            #     return render(request,'index.html',{'s_user':user})
    # else:
        return render(request,'index.html')

# @login_required(login_url='login')
class studentsignup(CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = 'studsignup.html'


    def form_valid(self, form):
        user=form.save()
        login(self.request)
        return redirect('login')

# @login_required(login_url='login')
class lectsignup(CreateView):
    model = User
    form_class = LecturerSignupForm
    template_name = 'lectsignup.html'

    def form_valid(self, form):
        user=form.save()
        login(self.request)
        return redirect('login')

# @login_required(login_url='login')
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                loginUser(request,user)
                if user.is_lecturer=='1':
                    return redirect('addlect')
                elif user.is_student=='2':
                    return redirect('addstud')
                else:
                    return redirect('main')
            else:
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid Username or password')

    return render(request,'login.html',{'form':AuthenticationForm()})



def signout(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
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
        sf = StudentForm(request.POST)
        ff=FeeForm(request.POST)
        if request.method == 'POST':
            user=request.user
            print(user)
            sf=StudentForm(request.POST)
            ff=FeeForm(request.POST)
            if sf.is_valid():
                sn = sf.cleaned_data['stu_name']
                print(sn)
                sf.save()

                if ff.is_valid():
                    ff.save()
                                    # Student.user=user
                # Student.save()
                # print(Student)
                return redirect('addstud')
            else:
                return render(request,'addstu.html',context={'form':sf,'ff':ff})
        else:
            return render(request, 'addstu.html', context={'form': sf,'ff':ff})


def student(request):
    stu=Student.objects.all()
    context={'stu':stu}
    return render(request,'student.html',context)


def deletestud(request,id):
    print(id)
    Student.objects.get(pk=id).delete()
    return redirect('student')
