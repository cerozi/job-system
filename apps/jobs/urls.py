from django.urls import path
from .views import job_create, job_update, job_close, total_jobs, total_company_jobs

urlpatterns = [
    path('company/create-job/', job_create, name='create-job'),
    path('company/update-job/<int:pk>', job_update, name='update-job'),
    path('company/close-job/<int:pk>', job_close, name='close-job'),
    path('company/jobs/', total_company_jobs, name='company-jobs'),
    path('employee/jobs/', total_jobs, name='employee-jobs'),
]