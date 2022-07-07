# django built-in imports;
from django.db.models.signals import post_save

# other apps imports;
from apps.apply.models import Apply
from apps.authentication.models import User
from apps.jobs.models import Job

# current app imports;
from .models import Notification

''' Signals for creating notifications. When a instance from the sender
model is created, a notification object is created. '''

def create_new_job_notification(sender, instance, created, **kwargs):
    ''' Creates notification object when a company user creates a new job object.
    :param - instance: instance that was created from the sender model;
    :param - created: boolean that returns True if the instance was created, not updated;
    '''

    if created:
        employee_qs = User.objects.filter(is_company=False)
        for employee in employee_qs:                              # creates a notification to each employee;
            Notification.objects.create(from_user=instance.company.user,
                                        to_user=employee,
                                        job=instance,
                                        notification_type="V")


def create_application_notification(sender, instance, created, **kwargs):     
    ''' Creates notification object when a employee user creates a new application object.
    :param - instance: instance that was created from the sender model;
    :param - created: boolean that returns True if the instance was created, not updated;
    '''

    if created:
        Notification.objects.create(from_user=instance.employee.user,
                                    to_user=instance.job.company.user,
                                    job=instance.job,
                                    notification_type="C")

post_save.connect(create_new_job_notification, sender=Job)
post_save.connect(create_application_notification, sender=Apply)
