# django built-in imports;
from django.contrib.auth.forms import UserCreationForm
from django import forms

# current app imports;
from .models import User

class CustomUserRegisterForm(UserCreationForm):
    # Custom form for user register;

    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}))
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', "class": "form-control", "placeholder": "Senha"}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', "class": "form-control", "placeholder": "Confirme a senha"}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_company')


class CustomUserLoginForm(forms.Form):
    # Custom form for user login;

    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', "class": "form-control", "placeholder": "Senha"}),
    )