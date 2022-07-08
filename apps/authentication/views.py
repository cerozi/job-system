# django built-in imports;
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_user
from django.contrib.auth import logout as log_out
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse


# current app imports;
from .decorators import only_unauthenticated_users
from .forms import CustomUserLoginForm, CustomUserRegisterForm


@only_unauthenticated_users
def register(request):
    ''' Creates a new user. '''

    form = CustomUserRegisterForm()
    status_code = 200
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # creates a new user object;
            messages.info(request, "Usuário registrado com sucesso. ")
            return redirect(reverse('login'))
        else:
            status_code = 422
            messages.info(request, "Credenciais inválidas. ")

    return render(request, 'home/register.html', {"form": form}, status=status_code)

@only_unauthenticated_users
def login(request):
    ''' Logs user. '''

    form = CustomUserLoginForm()
    status_code = 200
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            # authenticates the user, if both the email and password are right it returns the user object;
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                # logs the user;
                log_user(request, user)
                user_str = request.user.is_company_or_employee()
                return redirect(reverse(f'{user_str}-home'))
        
        status_code = 422
        
        messages.info(request, "Credenciais inválidas. ")
    return render(request, 'home/login.html', {"form": form}, status=status_code)


@login_required
def logout(request):
    ''' Logout the user. '''

    log_out(request)
    return redirect(reverse('login'))
