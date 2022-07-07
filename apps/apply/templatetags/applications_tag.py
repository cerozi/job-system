# built-in apps imports;
from django import template

# other apps imports;
from apps.apply.models import Apply
from apps.profiles.models import Employee, Company




register = template.Library()

# template tags for the cards on the home dashboard;

@register.simple_tag
def get_employee_applications(user):
    ''' Returns a integer that counts all the employee applications
    :param - user: user object
    :return - integer
     '''

    employee_obj = Employee.objects.get(user=user)
    return Apply.objects.filter(employee=employee_obj, job__closed=False).count()


@register.simple_tag
def get_company_applications_count(user):
    ''' Returns a integer that counts all the applications related to the company
    :param - user: user object
    :return - integer
     '''

    company_obj = Company.objects.get(user=user)
    return Apply.objects.filter(job__company=company_obj, job__closed=False).count()

@register.simple_tag
def get_job_applications_count(job):
    ''' Return all the applications related to the job
    :param - job: job object
    :return - integer
    '''
    return Apply.objects.filter(job=job).count()

# template tag for the applications page;

@register.simple_tag
def get_employee_points(application):
    ''' Return all the points from the application employee
    :param - application: application object
    :return - integer
    '''


    points = 0

    if int(application.job.scholarship) <= int(application.employee.scholarship):
        points += 1

    if application.job.salary == application.salary:
        points += 1

    return points