# built-in django imports;
from django.shortcuts import redirect
from django.urls import reverse

def only_unauthenticated_users(view_func):
    """decorator that allows only unauthenticated users to have access to the controller"""

    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect(reverse('employee-home'))

    return wrapper_func

def only_company_users(view_func):
    """decorator that allows only company users to have access to the controller, 
    which means that employee users can't access it"""

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_company:
            return view_func(request, *args, **kwargs)
        return redirect(reverse('employee-home'))

    return wrapper_func

def only_employee_users(view_func):
    """decorator that allows only employee users to have access to the controller, 
    which means that company users can't access it"""

    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_company:
            return view_func(request, *args, **kwargs)
        return redirect(reverse('company-home'))

    return wrapper_func