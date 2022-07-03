from django.db import models
from apps.authentication.models import User
from .validators import validate_only_number_field


class Company(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=8, validators=[validate_only_number_field], null=True)
    description = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Company'

class Employee(models.Model):
    SCHOLARSHIP_CHOICES = (
        ('0', 'Ensino Fundamental'),
        ('1', 'Ensino Médio'),
        ('2', 'Tecnólogo'),
        ('3', 'Ensino Superior'),
        ('4', 'Mestrado'),
        ('5', 'Doutorado')
    )

    ROLE_CHOICES = (
        ('F', 'FrontEnd'),
        ('B', 'BackEnd'),
        ('DB', 'Banco de Dados'),
        ('T', 'Tester'),
        ('DO', 'DevOps')
    )

    photo = models.ImageField(default='profile_pic/default.png', upload_to='profile_pic')
    name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True)
    tel = models.CharField(max_length=13, validators=[validate_only_number_field], null=True)
    address = models.CharField(max_length=150, null=True)
    scholarship = models.CharField(max_length=1, choices=SCHOLARSHIP_CHOICES, null=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, null=True)
    about_me = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.name}'

    def check_null_fields(self):
        if self.name and self.tel and self.scholarship and self.role:
            return True
        
        return None

    class Meta:
        verbose_name_plural = 'Employee'
