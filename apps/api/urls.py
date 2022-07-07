# django built-in imports;
from django.urls import path

# current app imports;
from .views import ApplicationsMonthAV, JobsMonthAv

urlpatterns = [
    path('api/applications', ApplicationsMonthAV.as_view(), name='api-applications'),
    path('api/jobs', JobsMonthAv.as_view(), name='api-jobs')
]