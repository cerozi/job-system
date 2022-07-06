from django.urls import path
from .views import ApplicationsMonthAV

urlpatterns = [
    path('api/applications', ApplicationsMonthAV.as_view())
]