# other apps imports;
from apps.authentication.models import User
# django built-in imports;
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class ProfilesViewTests(TestCase):
    ''' Tests the profiles app controllers. '''

    def setUp(self):
        self.client = Client()
        self.user_employee = User.objects.create_user(username='test_employee', 
        email='test_employee@gmail.com', password='userpass123', is_company=False)
        self.user_company = User.objects.create_user(username='test_company', 
        email='test_company@gmail.com', password='userpass123', is_company=True)

    def test_company_profile_get_method(self):
        self.client.login(email=self.user_company.email, password='userpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/company_profile.html')

    def test_company_profile_post_method_with_valid_data(self):
        self.client.login(email=self.user_company.email, password='userpass123')
        data = {
            'name': 'Cerozi Informática',
            'address': 'Rua do Limoeiro, 343',
            'city': 'São Paulo',
            'country': 'Brasil',
            'cep': '03089030',
            'description': 'Empresa de tecnologia/arquitetura web. '
        }

        self.assertIsNone(self.user_company.company.name)
        response = self.client.post(reverse('profile'), data=data)
        self.user_company.company.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(self.user_company.company.name)

    def test_company_profile_post_method_with_invalid_data(self):
        self.client.login(email=self.user_company.email, password='userpass123')
        response = self.client.post(reverse('profile'), data=None)
        self.assertEqual(response.status_code, 422)
        self.assertTemplateUsed(response, 'home/company_profile.html')

    def test_employee_profile_post_method_with_valid_data(self):
        self.client.login(email=self.user_employee.email, password='userpass123')
        data = {
            'name': 'Cerozi Informática',
            'address': 'Rua do Limoeiro, 343',
            'age': 20,
            'tel': '11995588963',
            'scholarship': '3',
            'role': 'B',
            'about_me': 'Python Dev.'
        }

        self.assertIsNone(self.user_employee.employee.name)
        response = self.client.post(reverse('profile'), data=data)
        self.user_employee.employee.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(self.user_employee.employee.name)
    
    def test_employee_profile_post_method_with_invalid_data(self):
        self.client.login(email=self.user_employee.email, password='userpass123')
        response = self.client.post(reverse('profile'), data=None)
        self.assertEqual(response.status_code, 422)
        self.assertTemplateUsed(response, 'home/user_profile.html')


    def test_employee_profile_get_method(self):
        self.client.login(email=self.user_employee.email, password='userpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/user_profile.html')
