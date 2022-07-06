from django.urls import path
from .views import ApplicationsMonthAV, JobsMonthAv

urlpatterns = [
    path('api/applications', ApplicationsMonthAV.as_view()),
    path('api/jobs', JobsMonthAv.as_view())
]