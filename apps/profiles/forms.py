# django built-in imports;
from django import forms

# current app imports;
from .models import Employee, Company

# custom form for employee profile;
class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('photo', 'name', 'age',
        'tel', 'address', 'scholarship', 'role', 'about_me')

        widgets = {
            'photo': forms.ClearableFileInput(attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome"}),
            'age': forms.TextInput(attrs={"class": "form-control", "placeholder": "Idade"}),
            'tel': forms.TextInput(attrs={"class": "form-control", "placeholder": "Telefone"}),
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Endereço"}),
            'scholarship': forms.Select(attrs={"class": "form-control"}),
            'role': forms.Select(attrs={"class": "form-control"}),
            'about_me': forms.TextInput(attrs={"class": "form-control", "placeholder": "Descreva-te."})
        }

# custom form for company profile;
class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'address', 
        'city', 'country', 'cep', 'description')

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome"}),
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Endereço"}),
            'city': forms.TextInput(attrs={"class": "form-control", "placeholder": "Cidade"}),
            'country': forms.TextInput(attrs={"class": "form-control", "placeholder": "País"}),
            'cep': forms.TextInput(attrs={"class": "form-control", "placeholder": "CEP"}),
            'description': forms.TextInput(attrs={"class": "form-control", "placeholder": "Descrição. "})
        }