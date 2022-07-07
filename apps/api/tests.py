# other apps imports;
from apps.authentication.models import User

# django built-in imports
from django.urls import reverse

# rest framework built-in imports
from rest_framework import status
from rest_framework.test import APITestCase


class ApiViewTest(APITestCase):
    ''' API VIEW tests. '''

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@gmail.com', 
                                            password='userpass123', is_company=True)
        self.client.force_authenticate(user=self.user)

    def test_get_applications_month_view(self):
        response = self.client.get(reverse('api-applications'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_jobs_month_view(self):
        response = self.client.get(reverse('api-jobs'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
