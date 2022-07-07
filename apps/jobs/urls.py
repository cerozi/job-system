 # django built-in imports;
from django.urls import path

 # current app imports;
from .views import (job_create, job_update, job_close, 
                    total_jobs, total_company_jobs, job_open, 
                    job_delete, search_job)

urlpatterns = [
    path('company/create-job/', job_create, name='create-job'),
    path('company/update-job/<int:pk>', job_update, name='update-job'),
    path('company/delete-job/<int:pk>', job_delete, name='delete-job'),
    path('company/close-job/<int:pk>', job_close, name='close-job'),
    path('company/open-job/<int:pk>', job_open, name='open-job'),
    path('company/jobs/', total_company_jobs, name='company-jobs'),
    path('employee/jobs/', total_jobs, name='employee-jobs'),
    path('search-job', search_job, name='search-job'),
]