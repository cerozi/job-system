from django.urls import path
from .views import create_apply, update_apply, delete_apply

urlpatterns = [
    path('apply/<int:pk>', create_apply, name='apply'),
    path('update/apply/<int:pk>', update_apply, name='update-apply'),
    path('delete/apply/<int:pk>', delete_apply, name='delete-apply')
]