# django built-in imports;
from django import forms

# current app imports;
from .models import Job

# Custom form for job creation;
class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 
                'salary', 
                'description',
                'scholarship')


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'salary': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Requisitos'}),
            'scholarship': forms.Select(attrs={'class': 'form-control'})
        }