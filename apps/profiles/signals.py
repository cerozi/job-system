from django.db.models.signals import post_save
from .models import Employee, Company
from apps.authentication.models import User


def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_company or instance.is_staff:
            instance.is_company = True
            instance.save()
            Company.objects.create(user=instance)
        else:
            Employee.objects.create(user=instance)

post_save.connect(create_profile, sender=User)