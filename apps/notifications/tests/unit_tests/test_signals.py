from django.test import TestCase
from apps.authentication.models import User
from apps.jobs.models import Job
from apps.notifications.models import Notification
from apps.apply.models import Apply

class NotificationsSignalsTests(TestCase):

    def setUp(self):
        self.user_company = User.objects.create_user(username='test_company', email='test@gmail.com', 
        password='userpass123', is_company=True)
        self.user_employee = User.objects.create_user(username='test_employee', email='test_employee@gmail.com', 
        password='userpass123')
        self.test_job = Job.objects.create(title='test_job', salary="a1", description='test',
        scholarship="3", company=self.user_company.company)

    def test_signals_creating_job_notification(self):
        self.assertEqual(len(Notification.objects.all()), 1)
        self.job = Job.objects.create(title='job', salary="a1", description='test',
        scholarship="3", company=self.user_company.company)
        self.assertEqual(len(Notification.objects.all()), 2)

    def test_signals_creating_application_notification(self):
        self.assertEqual(len(Notification.objects.all()), 1)
        self.apply = Apply.objects.create(job=self.test_job, employee=self.user_employee.employee, 
        salary="a1", experience='test')
        self.assertEqual(len(Notification.objects.all()), 2)