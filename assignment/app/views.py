from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from .forms import StudentForm


# Create your views here.
def show(request):
    sf = StudentForm()
    return render(request, 'index.html', {'form': sf})


def save(request):
    sf = StudentForm(request.POST)
    if sf.is_valid():
        name = sf.cleaned_data['name']
        email = sf.cleaned_data['email']
        age = sf.cleaned_data['age']
        phno = sf.cleaned_data['pno']
        dob = sf.cleaned_data['dob']
        sf.name = name
        sf.email = email
        sf.age = age
        sf.pno = phno
        sf.dob = dob
        sf.save()
        messages.success(request, "Details are saved")
        return redirect('search_emp')

    else:
        return render(request, 'index.html', {'form': sf})


def search_emp(request):
    if request.method == 'POST':
        emp = request.POST.get("s1")
        print(emp)
        try:
            res = Student.objects.filter(name__icontains=emp)
            print(res)
            return render(request, 'search.html', {'res': res})
        except Student.DoesNotExist:
            return render(request, "search.html", {'error': "Details Does Not Exist"})
    else:
        return render(request, 'search.html')
