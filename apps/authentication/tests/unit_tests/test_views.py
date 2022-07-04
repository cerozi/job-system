from django.test import TestCase
from django.test.client import Client
from apps.authentication.models import User
from django.urls import reverse
from django.contrib.auth import get_user

class AuthenticationViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='test_user', email='test@gmail.com',
        password='userpass123')


    def test_register_get_method(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/register.html')

    def test_register_post_method_with_valid_data(self):
        data = {
            'username': 'math',
            'email': 'math@gmail.com',
            'password1': 'testuser123',
            'password2': 'testuser123'
        }
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(User.objects.all()), 2)

    def test_register_post_method_with_invalid_data(self):
        response = self.client.post(reverse('register'), data=None)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(len(User.objects.all()), 1)
        self.assertTemplateUsed(response, 'home/register.html')

    def test_login_get_method(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/login.html')

    def test_login_post_method_with_valid_data(self):
        data = {
            'email': self.test_user.email,
            'password': 'userpass123'
        }

        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_login_post_method_with_invalid_data(self):
        response = self.client.post(reverse('login'), data=None)
        self.assertEqual(response.status_code, 422)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_logout(self):
        self.client.login(email=self.test_user.email, password='userpass123')
        self.assertTrue(get_user(self.client).is_authenticated)

        response = self.client.post(reverse('logout'))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(get_user(self.client).is_authenticated)