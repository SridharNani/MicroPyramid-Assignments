# from django.http import  HttpResponseRedirect
from django.core.exceptions import PermissionDenied

def role_requried(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request,*args,**kwargs):
            if request.role in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                raise PermissionDenied
        return wrap
    return decorator


def admin_or_lecturer_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_lecturer or not request.user.is_admin :
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner



def admin_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner


def lecturer_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_lecturer:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner

def student_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_student:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner

def staff_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner