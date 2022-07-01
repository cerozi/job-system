from django.db import models
from apps.profiles.models import Company
from apps.profiles.models import Employee

class Job(models.Model):
    SALARY_CHOICES = (
        ('a1', 'Até R$1.000,00'),
        ('1a2', 'De R$1.000,00 a R$2.000,00'),
        ('2a3', 'De R$2.000,00 a R$3.000,00'),
        ('3+', 'Acima de R$3.000,00')
    )


    title = models.CharField(max_length=100)
    salary = models.CharField(max_length=3, choices=SALARY_CHOICES)
    description = models.TextField()
    scholarship = models.CharField(max_length=1, choices=Employee.SCHOLARSHIP_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title} - {self.company}'