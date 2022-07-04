from django.test import TestCase
from apps.authentication.forms import CustomUserLoginForm, CustomUserRegisterForm

class AuthenticationFormsTests(TestCase):

    def test_register_form_with_valid_data(self):
        form = CustomUserRegisterForm(data={
            'username': 'math',
            'email': 'math@gmail.com',
            'password1': 'testuser123',
            'password2': 'testuser123'
        })

        self.assertTrue(form.is_valid())

    def test_register_form_with_invalid_data(self):
        form = CustomUserRegisterForm(data=None)

        self.assertFalse(form.is_valid())

    def test_login_form_with_valid_data(self):
        form = CustomUserLoginForm(data={
            'email': 'math@gmail.com',
            'password': 'userpass123'
        })

        self.assertTrue(form.is_valid())

    def test_login_form_with_invalid_data(self):
        form = CustomUserLoginForm(data=None)

        self.assertFalse(form.is_valid())