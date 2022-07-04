from django.db import models
from apps.jobs.models import Job
from apps.profiles.models import Employee

class Apply(models.Model):

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.CharField(max_length=3, choices=Job.SALARY_CHOICES)
    experience = models.TextField()

    class Meta:
        verbose_name_plural = 'Apply'
        unique_together = ['job', 'employee']

    def __str__(self) -> str:
        return f'{self.job} - {self.employee}'

    @classmethod
    def get_all_employee_applications(cls, user):
        employee = Employee.objects.get(user=user)
        applications = cls.objects.filter(employee=employee, job__closed=False)
        return applications