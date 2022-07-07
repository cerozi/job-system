# other apps imports;
from apps.authentication.models import User

# built-in django imports;
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class HomeViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user_employee = User.objects.create_user(username='test_employee_user',
        email='test_employee@gmail.com', password='userpass123')
        self.user_company = User.objects.create_user(username='test_company_user',
        email='test_company@gmail.com', password='userpass123', is_company=True)

    def test_get_method_employee_home(self):
        self.client.login(email=self.user_employee.email, password='userpass123')
        response = self.client.get(reverse('employee-home'))

        self.assertEqual(response.status_code, 200)
        self.client.logout()

        response = self.client.get(reverse('employee-home'))
        self.assertEqual(response.status_code, 302)

    def test_get_method_company_home(self):
        self.client.login(email=self.user_company.email, password='userpass123')
        response = self.client.get(reverse('company-home'))

        self.assertEqual(response.status_code, 200)
        self.client.logout()

        response = self.client.get(reverse('company-home'))
        self.assertEqual(response.status_code, 302)
