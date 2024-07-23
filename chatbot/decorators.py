from django.http import HttpResponse
from django.shortcuts import redirect


def authorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_admin:
            path = request.META["PATH_INFO"]
            return redirect(path)
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
