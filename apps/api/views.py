from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions as built_permissions
from apps.apply.models import Apply
from apps.profiles.models import Company
from .permissions import IsCompany


class ApplicationsMonthAV(APIView):
    permission_classes = [built_permissions.IsAuthenticated, IsCompany]

    def get(self, request, *args, **kwargs):
        month_applications = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        company_obj = Company.objects.get(user=self.request.user)
        company_applications = Apply.objects.filter(job__company=company_obj)

        for application in company_applications:
            application_month = application.created.strftime('%-m')
            month_applications[int(application_month) - 1] += 1

        data = {
            'month_applications': month_applications
        }
        return Response(data)