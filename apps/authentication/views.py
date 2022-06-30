from django.shortcuts import redirect, render
from .forms import CustomUserRegisterForm, CustomUserLoginForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, logout as log_out, login as log_user
from django.contrib.auth.decorators import login_required
from .decorators import only_unauthenticated_users

@only_unauthenticated_users
def register(request):
    form = CustomUserRegisterForm()
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Usuário registrado com sucesso. ")
            return redirect(reverse('login'))
        else:
            messages.info(request, "Credenciais inválidas. ")

    return render(request, 'home/register.html', {"form": form})

@only_unauthenticated_users
def login(request):
    form = CustomUserLoginForm()
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            print(user)
            if user:
                log_user(request, user)
                return redirect(reverse('employee-home'))
        
        messages.info(request, "Credenciais inválidas. ")
    return render(request, 'home/login.html', {"form": form})


@login_required
def logout(request):
    log_out(request)
    return redirect(reverse('login'))

def profile_view(request):
    return render(request, 'home/profile.html', {})
