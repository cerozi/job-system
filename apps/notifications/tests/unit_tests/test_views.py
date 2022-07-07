# other apps imports;
from apps.authentication.models import User
from apps.jobs.models import Job
from apps.notifications.models import Notification

# django built-in imports;
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class NotificationsViewTests(TestCase):
    ''' Tests the notifications controllers. '''

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
        self.assertIn(notification, Notification.objects.all())
        self.assertEqual(Notification.objects.all().count(), 1)
        
        response = self.client.get(reverse('delete-notifications'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(notification, Notification.objects.all())
        self.assertEqual(Notification.objects.all().count(), 0)
        
