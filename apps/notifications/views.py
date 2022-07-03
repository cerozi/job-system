from django.shortcuts import redirect
from apps.notifications.models import Notification
from django.urls import reverse

# Create your views here.
def delete_all_notifications(request):
    notifications = Notification.objects.filter(to_user=request.user, user_has_seen=False)
    for notification in notifications:
        notification.user_has_seen = True
        notification.save()

    return redirect(reverse('employee-home'))