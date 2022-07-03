from django.db.models.signals import post_save
from apps.jobs.models import Job
from apps.authentication.models import User
from .models import Notification
from apps.apply.models import Apply


def create_new_job_notification(sender, instance, created, **kwargs):
    if created:
        employee_qs = User.objects.filter(is_company=False)
        for employee in employee_qs:
            Notification.objects.create(from_user=instance.company.user,
                                        to_user=employee,
                                        job=instance,
                                        notification_type="V")


def create_application_notification(sender, instance, created, **kwargs):                                        
    if created:
        Notification.objects.create(from_user=instance.employee.user,
                                    to_user=instance.job.company.user,
                                    job=instance.job,
                                    notification_type="C")

post_save.connect(create_new_job_notification, sender=Job)
post_save.connect(create_application_notification, sender=Apply)