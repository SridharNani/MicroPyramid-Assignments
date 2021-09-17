from django.contrib import messages
from django.shortcuts import render,redirect

from cms.decorator import lecturer_only, admin_only, student_only, staff_only, \
    admin_or_lecturer_only
from .models import Lecturer,Student,User,Staff,College,Depart,Branch,Subject,Salary,Results,TimeTable
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import StudentSignupForm,LecturerForm,StudentForm,LecturerSignupForm,StaffForm,StaffSignupForm,\
    collegeForm,DepartmentForm,branchForm,subjectForm,salaryForm,ResultForm,TimetableForm
from django.views.generic import CreateView
from django.db.utils import IntegrityError

# @login_required(login_url='login')
def showindex(request):
        if request.user.is_authenticated:
            user=request.user
        return render(request,'index.html')

# @login_required(login_url='login')
class studentsignup(CreateView):
    # type = request.GET["type"]
    # type = request.GET.get("type")
    model = User
    form_class = StudentSignupForm
    template_name = 'studsignup.html'


    def form_valid(self, form):
        user=form.save(commit=False)
        user.is_student=True
        user.save()
        login(self.request)
        return redirect('login')

# @login_required(login_url='login')
class lectsignup(CreateView):
    model = User
    form_class = LecturerSignupForm
    template_name = 'lectsignup.html'

    def form_valid(self, form):
        user=form.save(commit=False)
        user.is_lecturer = True
        user.save()
        login(self.request)
        return redirect('login')

class staffsignup(CreateView):
    model = User
    form_class = StaffSignupForm
    template_name = 'stfsignup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff=True
        user.save()
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
@admin_only
# @lecturer_or_admin_only
def addlect(request):
    if request.user.is_authenticated:
        lf=LecturerForm(request.POST)
        if request.method=='POST':
            user=request.user
            # print(user)
            user=User.objects.get(username=request.POST.get('lecturer'))
            lr=Lecturer.objects.get(user_id=user.id)

            if lf.is_valid():
                # lf.cleaned_data['clg_name'] = "rakesh"
                lr.clg_name = lf.cleaned_data['clg_name']
                lr.dep_name=lf.cleaned_data['dep_name']
                lr.bran_name=lf.cleaned_data['bran_name']
                lr.lect_name=lf.cleaned_data['lect_name']
                lr.lect_sal=lf.cleaned_data['lect_sal']
                lr.subject=lf.cleaned_data['subject']
                lr.time_table=lf.cleaned_data['time_table']
                # Lecturer(user_id=lr.id,clg_name=lf.cleaned_data['clg_name'],
                #          dep_name=lf.cleaned_data['dep_name'],
                #          bran_name=lf.cleaned_data['bran_name'],
                #          lect_name=lf.cleaned_data['lect_name'],
                #          lect_sal=lf.cleaned_data['lect_sal'],
                #          subject=lf.cleaned_data['subject'],
                #          time_table=lf.cleaned_data['time_table']).save()
                # lr=Lecturer(user_id=User.objects.get(username=request.POST.get('lecturer')))
                lr.save()
                # print(Lecturer)
                return redirect('lecturer')
            else:
                return render(request,'addlect.html',context={'form':lf, 'lecturers':User.objects.filter(is_lecturer=True)})
                # return render(request,'addlect.html',context={'form':lf})
        else:
            return render(request, 'addlect.html', context={'form': lf, 'lecturers':User.objects.filter(is_lecturer=True)})

# @login_required(login_url='login')
@admin_only
def lecturer(request):
    lect = Lecturer.objects.all()
    context={'lect':lect}
    return render(request, 'lecturer.html', context)

# @login_required(login_url='login')
@lecturer_only
def onelecturer(request):
    lect = Lecturer.objects.get(user_id=request.user.id)
    context = {'lect': lect}
    return render(request, 'onelecturer.html', context)

# @login_required(login_url='login')
@admin_only
def deletelect(request,id):
    print(id)
    Lecturer.objects.get(pk=id).delete()
    return redirect('lecturer')

# @admin_or_lecturer_only
@lecturer_only
# @admin_only
def addstud(request):
    if request.user.is_authenticated:
        sf = StudentForm(request.POST)
        if request.method == 'POST':
            user=request.user
            # print(user)
            au=User.objects.get(username=request.POST.get('student'))
            st=Student.objects.get(user_id=au.id)

            if sf.is_valid():
                st.clg_name=sf.cleaned_data['clg_name']
                st.dep_name=sf.cleaned_data['dep_name']
                st.bran_name=sf.cleaned_data['bran_name']
                st.stu_name=sf.cleaned_data['stu_name']
                st.subject=sf.cleaned_data['subject']

                st.time_table=sf.cleaned_data['time_table']
                st.coll_fee=sf.cleaned_data['coll_fee']
                st.exam_fee=sf.cleaned_data['exam_fee']
                st.result=sf.cleaned_data['result']
                st.save()
                return redirect('student')
            else:
                return render(request,'addstu.html',context={'form':sf, 'students':User.objects.filter(is_student=True)})
        else:
            return render(request, 'addstu.html', context={'form': sf, 'students':User.objects.filter(is_student=True)})


# @login_required(login_url='login')
# @admin_or_lecturer_only
@lecturer_only
# @admin_only
def student(request):
    stu=Student.objects.all()
    context={'stu':stu}
    return render(request,'student.html',context)

# @login_required(login_url='login')
@lecturer_only
# @admin_only
# @admin_or_lecturer_only
def deletestud(request,id):
    print(id)
    Student.objects.get(pk=id).delete()
    return redirect('student')

# @login_required(login_url='login')
@student_only
def onestudent(request):
    stu = Student.objects.get(user_id=request.user.id)
    context = {'stu': stu}
    return render(request, 'onestudent.html', context)


# @login_required(login_url='login')
@admin_only
def addataff(request):
    if request.user.is_authenticated:
        stf = StaffForm(request.POST)
        if request.method == 'POST':
            user = request.user
            # print(user)
            user=User.objects.get(username=request.POST.get('staff'))
            sf=Staff.objects.get(user_id=user.id)
            if stf.is_valid():
                sf.clg_name=stf.cleaned_data['clg_name']
                sf.name=stf.cleaned_data['name']
                sf.staff_role=stf.cleaned_data['staff_role']
                sf.staff_salary=stf.cleaned_data['staff_salary']
                sf.save()
                return redirect('staff')
            else:
                return render(request, 'addstaff.html', context={'form': stf, 'staffs':User.objects.filter(is_staff=True)})
        else:
            return render(request, 'addstaff.html', context={'form': stf, 'staffs':User.objects.filter(is_staff=True)})


# @login_required(login_url='login')
@admin_only
def staff(request):
    stf = Staff.objects.all()
    print(stf)
    context = {'stf': stf}
    return render(request, 'staff.html', context)


# @login_required(login_url='login')
@staff_only
def onestaff(request):
    stf = Staff.objects.get(user_id=request.user.id)
    context = {'stf': stf}
    return render(request, 'onestaff.html', context)

# @login_required(login_url='login')
@admin_only
def delstaff(request,id):
    print(id)
    Staff.objects.get(pk=id).delete()
    return redirect('staff')

# @login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
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

# @login_required(login_url='login')
def college(request):
    if request.user.is_authenticated:
        clg = College.objects.all()
        print(clg)
        context = {'clg': clg}
        return render(request, 'college.html', context)

# @login_required(login_url='login')
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


# @login_required(login_url='login')
def department(request):
    if request.user.is_authenticated:
        dep = Depart.objects.all()
        print(dep)
        context = {'dep': dep}
        return render(request, 'department.html', context)


# @login_required(login_url='login')
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

# @login_required(login_url='login')
def branch(request):
    if request.user.is_authenticated:
        brn = Branch.objects.all()
        context = {'brn': brn}
        return render(request, 'branch.html', context)


# @login_required(login_url='login')
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

# @login_required(login_url='login')
def subject(request):
    sub = Subject.objects.all()
    context = {'sub': sub}
    return render(request, 'subject.html', context)


# @login_required(login_url='login')
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


# @login_required(login_url='login')
def salary(request):
    sal = Salary.objects.all()
    context = {'sal': sal}
    return render(request, 'salary.html', context)


# @login_required(login_url='login')
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

# @login_required(login_url='login')
def results(request):
    res = Results.objects.all()
    context = {'res': res}
    return render(request, 'result.html', context)


# @login_required(login_url='login')
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

# @login_required(login_url='login')
def timetable(request):
    tt = TimeTable.objects.all()
    context = {'tt': tt}
    return render(request, 'timetable.html', context)

