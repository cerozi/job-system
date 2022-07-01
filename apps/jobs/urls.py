from django.urls import path
from .views import job_create, job_update, job_close

urlpatterns = [
    path('create-job/', job_create, name='create-job'),
    path('update-job/<int:pk>', job_update, name='update-job'),
    path('close-job/<int:pk>', job_close, name='close-job')
]