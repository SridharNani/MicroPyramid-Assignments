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
from collegemanagementsystem import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showindex,name='main'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),

    #lecturer
    path('addlect/',views.addlect,name='addlect'),
    path('lecturer/',views.lecturer,name='lecturer'),
    path('deletelect/<int:id>',views.deletelect,name='deletelect'),

    #Student
    path('addstud/',views.addstud,name='addstud'),
    path('student/',views.student,name='student'),
    path('deletestud/<int:id>',views.deletestud,name='deletestud'),

    path('logout/',views.signout,name='signout')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
