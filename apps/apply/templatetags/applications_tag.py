from django import template
from apps.apply.models import Apply
from apps.profiles.models import Employee

register = template.Library()

@register.simple_tag
def get_employee_applications(user):
    employee_obj = Employee.objects.get(user=user)
    return Apply.objects.filter(employee=employee_obj).count()