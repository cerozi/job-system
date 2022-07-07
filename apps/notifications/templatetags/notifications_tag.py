# django built-in imports;
from django import template

# other apps imports;
from apps.notifications.models import Notification

register = template.Library()


# renders a template with all the notifications related to the request user;
@register.inclusion_tag('home/notifications.html', takes_context=True)
def show_notifications(context):
    user = context['request'].user
    notifications = Notification.objects.filter(to_user=user, user_has_seen=False)
    
    return {'notifications': notifications}