# django built-in imports;
from django.db import models

# other apps imports;
from apps.jobs.models import Job
from apps.profiles.models import Employee

class Apply(models.Model):

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.CharField(max_length=3, choices=Job.SALARY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    experience = models.TextField()

    class Meta:
        verbose_name_plural = 'Apply'
        unique_together = ['job', 'employee'] # employee can't apply to the same job;

    def __str__(self) -> str:
        return f'{self.job} - {self.employee}'

    @classmethod
    def get_all_employee_applications(cls, user):
        ''' Returns all the open applications from the user employee parameter. 
        :param - user: user object
        :return - applications queryset
        '''

        employee = Employee.objects.get(user=user)
        applications = cls.objects.filter(employee=employee, job__closed=False).order_by('-created')
        return applications