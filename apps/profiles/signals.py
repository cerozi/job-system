# django built-in imports;
from django.db.models.signals import post_save
# other apps imports;
from apps.authentication.models import User
# current app imports;
from .models import Company, Employee


def create_profile(sender, instance, created, **kwargs):
    ''' Creates a profile object related to the user object. 
    :param - instance: instance that was created from the sender model;
    :param - created: boolean that returns True if the instance was created, not updated;
    '''

    if created:
        if instance.is_company or instance.is_staff:
            instance.is_company = True
            instance.save()
            Company.objects.create(user=instance, name=instance.username)
        else:
            Employee.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
