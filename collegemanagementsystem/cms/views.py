from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Lecturer,Student,User,Staff
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import StudentSignupForm,LecturerForm,StudentForm,LecturerSignupForm,StaffForm,StaffSignupForm
from django.views.generic import CreateView


# @login_required(login_url='login')
def showindex(request):
        if request.user.is_authenticated:
            user=request.user
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

class staffsignup(CreateView):
    model = User
    form_class = StaffSignupForm
    template_name = 'stfsignup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request)
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
                # if user.is_admin:
                #     return redirect('main')
                if user.is_lecturer:
                    return redirect('lecturer')
                elif user.is_student:
                    return redirect('student')
                elif user.is_staff:
                    return redirect('onestaff')
                else:
                    return redirect('main')

            else:
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid Username or password')

    return render(request,'login.html',{'form':AuthenticationForm()})




# @login_required(login_url='login')
def addlect(request):
    # if request.user.is_authenticated:
    #     user=request.user
    #     print(user)
        lf=LecturerForm(request.POST)
        if lf.is_valid():
            print(lf.cleaned_data)
            Lecturer=lf.save(commit=False)
            # Lecturer.user=user
            Lecturer.save()
            print(Lecturer)
            return redirect('lecturer')
        else:
            return render(request,'addlect.html',context={'form':lf})

def lecturer(request):
    lect = Lecturer.objects.all()
    # stu=Student.objects.all()
    context={'lect':lect}
    return render(request, 'lecturer.html', context)


def onelecturer(request):
    lect = Lecturer.objects.get(user_id=request.user.id)
    context = {'lect': lect}
    return render(request, 'onelecturer.html', context)


def deletelect(request,id):
    print(id)
    Lecturer.objects.get(pk=id).delete()
    return redirect('lecturer')

# @login_required(login_url='login')
def addstud(request):
    # import pdb;pdb.set_trace()
    if request.user.is_authenticated:
        sf = StudentForm(request.POST)
        if request.method == 'POST':
            user=request.user
            print(user)
            if sf.is_valid():
                sf.save()
                return redirect('student')
            else:
                return render(request,'addstu.html',context={'form':sf})
        else:
            return render(request, 'addstu.html', context={'form': sf})


def student(request):
    stu=Student.objects.all()
    context={'stu':stu}
    return render(request,'student.html',context)


def deletestud(request,id):
    print(id)
    Student.objects.get(pk=id).delete()
    return redirect('student')


def onestudent(request):
    stu = Student.objects.get(user_id=request.user.id)
    context = {'stu': stu}
    return render(request, 'onestudent.html', context)



def addataff(request):
    if request.user.is_authenticated:
        sf = StaffForm(request.POST)
        if request.method == 'POST':
            user = request.user
            print(user)
            if sf.is_valid():
                sf.save()
                return redirect('staff')
            else:
                return render(request, 'addstaff.html', context={'form': sf})
        else:
            return render(request, 'addstaff.html', context={'form': sf})


def staff(request):
    stf = Staff.objects.all()
    context = {'stf': stf}
    return render(request, 'staff.html', context)


def onestaff(request):
    staff = Staff.objects.get(user_id=request.user.id)
    context = {'stf': staff}
    return render(request, 'onestaff.html', context)

def delstaff(request,id):
    print(id)
    Staff.objects.get(pk=id).delete()
    return redirect('staff')


def signout(request):
    logout(request)
    return redirect('login')

