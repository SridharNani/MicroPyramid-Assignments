"""collegemanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cms import views
from cms.views import studentsignup,lectsignup
from collegemanagementsystem import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showindex,name='main'),
    path('login/',views.login,name='login'),


    #signup
    path('lsignup/',views.lectsignup.as_view(),name='lsignup'),
    path('stsignup/', views.studentsignup.as_view(), name='studsignup'),
    path('stfsignup/', views.staffsignup.as_view(), name='staffsignup'),


    #lecturer
    path('addlect/',views.addlect,name='addlect'),
    path('lecturer/',views.lecturer,name='lecturer'),
    path('onelecturer/',views.onelecturer,name='onelect'),
    path('deletelect/<int:id>',views.deletelect,name='deletelect'),


    #Student
    path('addstud/',views.addstud,name='addstud'),
    path('student/',views.student,name='student'),
    path('onestudent/',views.onestudent,name='onestud'),
    path('deletestud/<int:id>',views.deletestud,name='deletestud'),



    #staff
    path('addstaff/',views.addataff,name='addstaff'),
    path('staff/',views.staff,name='staff'),
    path('onestaff/',views.onestaff,name='onestaff'),
    path('deletestaff/<int:id>',views.delstaff,name='deletestaff'),

    #college
    path('addclg/',views.addclg,name='addclg'),
    path('college/',views.college,name='college'),


    #department
    path('adddep/',views.adddep,name='adddep'),
    path('department/',views.department,name='department'),


    #Branch
    path('addbrn/',views.addbrn,name='addbrn'),
    path('branch/',views.branch,name='branch'),


    # subject
    path('addsub/', views.addsub, name='addsub'),
    path('subject/', views.subject, name='subject'),


    # salary
    path('addsal/', views.addsal, name='addsal'),
    path('salary/', views.salary, name='salary'),


    #Results
    path('addres/',views.addres,name='addres'),
    path('results/',views.results,name='results'),

    #Time Table
    path('addtt/',views.addtt,name='addtt'),
    path('timetable/',views.timetable,name='timetable'),



    #logout
    path('logout/',views.signout,name='signout')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
