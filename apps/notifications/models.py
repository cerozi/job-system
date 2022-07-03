from secrets import choice
from django.db import models
from apps.authentication.models import User
from apps.jobs.models import Job

# Create your models here.
class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ("V", "Vaga"),
        ("C", "Candidatura")
    )

    notification_type = models.CharField(max_length=1, choices=NOTIFICATION_TYPES)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    user_has_seen = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.get_notification_type_display} - {self.from_user}'