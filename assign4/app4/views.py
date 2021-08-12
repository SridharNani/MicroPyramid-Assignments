from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,RedirectView,ListView,UpdateView,DeleteView,FormView
# Create your views here.
from .forms import StudentForm
from .models import Student
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class viewall(ListView):
    template_name = 'index.html'
    queryset = Student.objects.all()
    success_url= reverse_lazy('add')



class add(SuccessMessageMixin,FormView):
    form_class = StudentForm
    template_name = 'add.html'


    def form_valid(self, form):
        nm = form.cleaned_data['name']
        ag = form.cleaned_data['age']
        cn = form.cleaned_data['contact']
        em = form.cleaned_data['email']
        im = form.cleaned_data['image']
        reg = Student(name=nm, age=ag, contact=cn, email=em, image=im)
        reg.save()
        return render(self.request,'index.html',self.get_context_data())




class update(UpdateView):
    template_name = 'update.html'
    model = Student
    fields = "__all__"
    success_url = reverse_lazy('add')


class delete(DeleteView):
    template_name = 'delete.html'
    model = Student
    success_url = reverse_lazy('add')

