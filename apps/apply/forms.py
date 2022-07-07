# django built-in imports;
from django import forms

# current app imports;
from .models import Apply

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('salary', 'experience')

        widgets = {
            'salary': forms.Select(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experiência'})
        }