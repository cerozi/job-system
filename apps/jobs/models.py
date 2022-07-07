# django built-in imports;
from django.db import models

# other apps imports;
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

    @classmethod
    def get_company_active_jobs(cls, user):
        ''' Get all the active jobs from the received user parameter.
        :param - user: user object
        '''

        company_obj = Company.objects.get(user=user)
        return cls.objects.filter(company=company_obj, closed=False)

    @classmethod
    def get_company_all_jobs(cls, user):
        ''' Get all the jobs from the user parameter.
        :param - user: user object
        '''

        company_obj = Company.objects.get(user=user)
        return cls.objects.filter(company=company_obj)

    def get_job_all_employee_applications(self):
        ''' Returns a list with all the employees the applied to the job object. '''

        employee_list = [application.employee for application in self.apply_set.all()]
        return employee_list