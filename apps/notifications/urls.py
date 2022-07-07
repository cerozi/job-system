# django built-in imports;
from django.urls import path

# current app imports.
from .views import delete_all_notifications

urlpatterns = [
    path('delete-notifications', delete_all_notifications, name='delete-notifications')
]