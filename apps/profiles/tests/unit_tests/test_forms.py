from django.test import TestCase
from apps.profiles.forms import EmployeeProfileForm, CompanyProfileForm

class ProfileFormsTests(TestCase):

    def test_employee_form_with_valid_data(self):
        form = EmployeeProfileForm(data={
            'name': 'Cerozi Informática',
            'address': 'Rua do Limoeiro, 343',
            'age': 20,
            'tel': '11995588963',
            'scholarship': '3',
            'role': 'B',
            'about_me': 'Python Dev.'
        })

        self.assertTrue(form.is_valid())

    def test_employee_form_with_invalid_data(self):
        form = EmployeeProfileForm(data=None)

        self.assertFalse(form.is_valid())

    def test_company_form_with_valid_data(self):
        form = CompanyProfileForm(data={
            'name': 'Cerozi Informática',
            'address': 'Rua do Limoeiro, 343',
            'city': 'São Paulo',
            'country': 'Brasil',
            'cep': '03089030',
            'description': 'Empresa de tecnologia/arquitetura web. '
        })

        self.assertTrue(form.is_valid())

    def test_company_form_with_invalid_data(self):
        form = CompanyProfileForm(data=None)

        self.assertFalse(form.is_valid())