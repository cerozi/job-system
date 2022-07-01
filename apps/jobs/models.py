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
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.title} - {self.company}'

    def get_company_active_jobs(user):
        company_obj = Company.objects.get(user=user)
        return Job.objects.filter(company=company_obj, closed=False)

    def get_company_all_jobs(user):
        company_obj = Company.objects.get(user=user)
        return Job.objects.filter(company=company_obj)