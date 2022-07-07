# other apps imports;
from apps.authentication.models import User
from apps.profiles.models import Company, Employee

# django built-in imports;
from django.test import TestCase


class ProfileSignalsTest(TestCase):
    ''' Tests profiles app signals. '''

    def setUp(self):
        self.user_employee = User.objects.create_user(username='test_employee', 
        email='test_employee@gmail.com', password='userpass123', is_company=False)
        self.user_company = User.objects.create_user(username='test_company', 
        email='test_company@gmail.com', password='userpass123', is_company=True)

    def test_signals_creating_company_profile(self):
        self.assertTrue(hasattr(self.user_company, 'company'))
        self.assertIsInstance(self.user_company.company, Company)

    def test_signals_creating_employee_profile(self):
        self.assertTrue(hasattr(self.user_employee, 'employee'))
        self.assertIsInstance(self.user_employee.employee, Employee)
