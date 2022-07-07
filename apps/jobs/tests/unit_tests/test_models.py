# other apps imports;
from apps.apply.models import Apply
from apps.authentication.models import User
from apps.jobs.models import Job

# django built-in imports;
from django.test import TestCase


class JobsModelTests(TestCase):
    ''' Tests all the job model functions. '''

    def setUp(self):
        self.user_company = User.objects.create_user(username='test_company', email='test@gmail.com', 
        password='userpass123', is_company=True)
        self.user_employee = User.objects.create_user(username='test_employee', email='test_employee@gmail.com', 
        password='userpass123')
        self.open_job = Job.objects.create(title='open_job', salary="a1", description='test',
        scholarship="3", company=self.user_company.company)
        self.closed_job = Job.objects.create(title='closed_job', salary="a1", description='test',
        scholarship="3", company=self.user_company.company, closed=True)
        self.application = Apply.objects.create(job=self.open_job, employee=self.user_employee.employee, 
        salary="a1", experience='test')
    
    def test_get_company_active_jobs(self):
        active_jobs = Job.get_company_active_jobs(self.user_company)
        self.assertEqual(len(active_jobs), 1)
        self.assertIn(self.open_job, active_jobs)
        self.assertNotIn(self.closed_job, active_jobs)

    def test_get_company_all_jobs(self):
        all_jobs = Job.get_company_all_jobs(self.user_company)
        self.assertEqual(len(all_jobs), 2)
        self.assertIn(self.open_job, all_jobs)
        self.assertIn(self.closed_job, all_jobs)

    def test_get_job_all_employee_applications(self):
        employee_list = self.open_job.get_job_all_employee_applications()
        self.assertEqual(len(employee_list), 1)
        self.assertIn(self.user_employee.employee, employee_list)
