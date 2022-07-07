# other apps imports;
from apps.jobs.models import Job
from apps.profiles.models import Company

# django built-in imports;
from django import template

register = template.Library()

# template tags for home dashboard;

@register.simple_tag
def get_total_jobs(user):
    ''' Returns a quantity related to all the jobs from the received user company object.
    :param - user: user object
    :return - int
    '''

    company = Company.objects.get(user=user)
    return Job.objects.filter(company=company).count()

@register.simple_tag
def get_total_open_jobs(user):
    ''' Returns a quantity related to all the open jobs from the received user company object.
    :param - user: user object
    :return - int
    '''
    
    company = Company.objects.get(user=user)
    return Job.objects.filter(company=company, closed=False).count()

@register.simple_tag
def get_total_closed_jobs(user):
    ''' Returns a quantity related to all closed jobs from the received user company object.
    :param - user: user object
    :return - int
    '''

    company = Company.objects.get(user=user)
    return Job.objects.filter(company=company, closed=True).count()
