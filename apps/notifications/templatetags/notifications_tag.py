from django import template


from apps.notifications.models import Notification

register = template.Library()

@register.inclusion_tag('home/notifications.html', takes_context=True)
def show_notifications(context):
    user = context['request'].user
    notifications = Notification.objects.filter(to_user=user, user_has_seen=False)
    
    return {'notifications': notifications}