from django.test import TestCase
from apps.authentication.models import User
from apps.jobs.models import Job
from apps.apply.models import Apply

class ApplicationModelTests(TestCase):

    def setUp(self):
        self.user_company = User.objects.create_user(username='test_company', 
        email='test_company@gmail.com', password='userpass123', is_company=True)
        self.user_employee = User.objects.create_user(username='test_employee', 
        email='test_employee@gmail.com', password='userpass123', is_company=False)
        self.user_employee.employee.set_fields_to_test()

        self.test_job = Job.objects.create(title='test_job', salary="a1", description='test',
        scholarship="3", company=self.user_company.company)
        self.test_application = Apply.objects.create(job=self.test_job, employee=self.user_employee.employee, 
        salary="a1", experience='test')

    def test_get_all_employee_applications(self):
        applications = Apply.get_all_employee_applications(self.user_employee)

        self.assertEqual(len(applications), 1)
        self.assertIn(self.test_application, applications)