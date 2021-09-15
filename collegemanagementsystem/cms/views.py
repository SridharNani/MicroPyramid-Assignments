from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Lecturer,Student,User,Staff,College,Depart,Branch,Subject,Salary,Results,TimeTable
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import StudentSignupForm,LecturerForm,StudentForm,LecturerSignupForm,StaffForm,StaffSignupForm,\
    collegeForm,DepartmentForm,branchForm,subjectForm,salaryForm,ResultForm,TimetableForm
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
                if user.is_admin:
                    return redirect('main')
                if user.is_lecturer:
                    return redirect('onelect')
                elif user.is_student:
                    return redirect('onestud')
                elif user.is_staff:
                    return redirect('onestaff')
                else:
                    return redirect('main')

            else:
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid Username or password')

    return render(request,'login.html',{'form':AuthenticationForm()})




@login_required(login_url='login')
def addlect(request):
    if request.user.is_authenticated:
        lf=LecturerForm(request.POST)
        if request.method=='POST':
            user=request.user
            print(user)
            if lf.is_valid():
                lf.save()
                print(Lecturer)
                return redirect('lecturer')
            else:
                return render(request,'addlect.html',context={'form':lf, 'lecturers':Lecturer.objects.all()})
        else:
            return render(request, 'addlect.html', context={'form': lf, 'lecturers':Lecturer.objects.all()})

@login_required(login_url='login')
def lecturer(request):
    lect = Lecturer.objects.all()
    context={'lect':lect}
    return render(request, 'lecturer.html', context)

@login_required(login_url='login')
def onelecturer(request):
    lect = Lecturer.objects.get(user_id=request.user.id)
    context = {'lect': lect}
    return render(request, 'onelecturer.html', context)

@login_required(login_url='login')
def deletelect(request,id):
    print(id)
    Lecturer.objects.get(pk=id).delete()
    return redirect('lecturer')

@login_required(login_url='login')
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
                return render(request,'addstu.html',context={'form':sf, 'students':Student.objects.all()})
        else:
            return render(request, 'addstu.html', context={'form': sf, 'students':Student.objects.all()})

@login_required(login_url='login')
def student(request):
    stu=Student.objects.all()
    context={'stu':stu}
    return render(request,'student.html',context)

@login_required(login_url='login')
def deletestud(request,id):
    print(id)
    Student.objects.get(pk=id).delete()
    return redirect('student')

@login_required(login_url='login')
def onestudent(request):
    stu = Student.objects.get(user_id=request.user.id)
    context = {'stu': stu}
    return render(request, 'onestudent.html', context)


@login_required(login_url='login')
def addataff(request):
    if request.user.is_authenticated:
        stf = StaffForm(request.POST)
        if request.method == 'POST':
            user = request.user
            print(user)
            if stf.is_valid():
                stf.save()
                return redirect('staff')
            else:
                return render(request, 'addstaff.html', context={'form': stf, 'staffs':Staff.objects.all()})
        else:
            return render(request, 'addstaff.html', context={'form': stf, 'staffs':Staff.objects.all()})


@login_required(login_url='login')
def staff(request):
    stf = Staff.objects.all()
    print(stf)
    context = {'stf': stf}
    return render(request, 'staff.html', context)


@login_required(login_url='login')
def onestaff(request):
    stf = Staff.objects.get(user_id=request.user.id)
    context = {'stf': stf}
    return render(request, 'onestaff.html', context)

@login_required(login_url='login')
def delstaff(request,id):
    print(id)
    Staff.objects.get(pk=id).delete()
    return redirect('staff')

@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def addclg(request):
    if request.user.is_authenticated:
        clg = collegeForm(request.POST)
        if request.method == 'POST':
            user = request.user
            print(user)
            if clg.is_valid():
                clg.save()
                return redirect('college')
            else:
                return render(request, 'addclg.html', context={'form': clg})
        else:
            return render(request, 'addclg.html', context={'form': clg})

@login_required(login_url='login')
def college(request):
    if request.user.is_authenticated:
        clg = College.objects.all()
        print(clg)
        context = {'clg': clg}
        return render(request, 'college.html', context)

@login_required(login_url='login')
def adddep(request):
    if request.user.is_authenticated:
        dep = DepartmentForm(request.POST)
        print(dep)
        if request.method == 'POST':
            user = request.user
            print(user)
            if dep.is_valid():
                dep.save()
                print(dep.cleaned_data["id"])
                print(dep.cleaned_data["clg_name"])
                print(dep.cleaned_data["dep_name"])
                return redirect('department')
            else:
                return render(request, 'adddep.html', context={'form': dep})
        else:
            return render(request, 'adddep.html', context={'form': dep})


@login_required(login_url='login')
def department(request):
    if request.user.is_authenticated:
        dep = Depart.objects.all()
        print(dep)
        context = {'dep': dep}
        return render(request, 'department.html', context)


@login_required(login_url='login')
def addbrn(request):
    if request.user.is_authenticated:
        brn = branchForm(request.POST)
        print(brn)
        if request.method == 'POST':
            user = request.user
            print(user)
            if brn.is_valid():
                brn.save()
                return redirect('branch')
            else:
                return render(request, 'addbrn.html', context={'form': brn})
        else:
            return render(request, 'addbrn.html', context={'form': brn})

@login_required(login_url='login')
def branch(request):
    if request.user.is_authenticated:
        brn = Branch.objects.all()
        context = {'brn': brn}
        return render(request, 'branch.html', context)


@login_required(login_url='login')
def addsub(request):
    if request.user.is_authenticated:
        sub = subjectForm(request.POST)
        if request.method == 'POST':
            user = request.user
            print(user)
            if sub.is_valid():
                sub.save()
                return redirect('subject')
            else:
                return render(request, 'addsub.html', context={'form': sub})
        else:
            return render(request, 'addsub.html', context={'form': sub})

@login_required(login_url='login')
def subject(request):
    sub = Subject.objects.all()
    context = {'sub': sub}
    return render(request, 'subject.html', context)


@login_required(login_url='login')
def addsal(request):
    if request.user.is_authenticated:
        sal = salaryForm(request.POST)
        if request.method == 'POST':
            user = request.user
            print(user)
            if sal.is_valid():
                sal.save()
                return redirect('salary')
            else:
                return render(request, 'addsal.html', context={'form': sal})
        else:
            return render(request, 'addsal.html', context={'form': sal})


@login_required(login_url='login')
def salary(request):
    sal = Salary.objects.all()
    context = {'sal': sal}
    return render(request, 'salary.html', context)


@login_required(login_url='login')
def addres(request):
    if request.user.is_authenticated:
        res = ResultForm(request.POST)
        if request.method == 'POST':
            user = request.user
            print(user)
            if res.is_valid():
                res.save()
                return redirect('results')
            else:
                return render(request, 'addres.html', context={'form': res})
        else:
            return render(request, 'addres.html', context={'form': res})

@login_required(login_url='login')
def results(request):
    res = Results.objects.all()
    context = {'res': res}
    return render(request, 'result.html', context)


@login_required(login_url='login')
def addtt(request):
    if request.user.is_authenticated:
        tt = TimetableForm(request.POST)
        if request.method == 'POST':
            user = request.user
            print(user)
            if tt.is_valid():
                tt.save()
                return redirect('timetable')
            else:
                return render(request, 'addtt.html', context={'form': tt})
        else:
            return render(request, 'addtt.html', context={'form': tt})

@login_required(login_url='login')
def timetable(request):
    tt = TimeTable.objects.all()
    context = {'tt': tt}
    return render(request, 'timetable.html', context)

