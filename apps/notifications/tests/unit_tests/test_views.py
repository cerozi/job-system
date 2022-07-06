from django.test import TestCase
from django.test.client import Client
from apps.authentication.models import User
from apps.jobs.models import Job
from apps.notifications.models import Notification
from django.urls import reverse

class NotificationsViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_company = User.objects.create_user(username='test_company', email='test@gmail.com', 
        password='userpass123', is_company=True)
        self.user_employee = User.objects.create_user(username='test_employee', email='test_employee@gmail.com', 
        password='userpass123')
        self.job = Job.objects.create(title='test_job', salary="a1", description='test',
        scholarship="3", company=self.user_company.company)

        self.client.login(email=self.user_employee.email, password='userpass123')

    def test_delete_all_notifications(self):
        notification = Notification.objects.get(job=self.job, to_user=self.user_employee, from_user=self.user_company)
        self.assertFalse(notification.user_has_seen)

        response = self.client.get(reverse('delete-notifications'))
        self.assertEqual(response.status_code, 302)
        notification.refresh_from_db()
        self.assertTrue(notification.user_has_seen)