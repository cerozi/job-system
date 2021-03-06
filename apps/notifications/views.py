# built-in django imports;
from django.shortcuts import redirect
from django.urls import reverse

# other apps imports;
from apps.notifications.models import Notification


def delete_all_notifications(request):
    ''' Deletes all the user notifications. '''

    notifications = Notification.objects.filter(to_user=request.user, user_has_seen=False)
    for notification in notifications:
        notification.delete() # deletes the notification object;

    user_str = request.user.is_company_or_employee()
    return redirect(reverse(f'{user_str}-home'))
