from django.test import TestCase
from django.test.client import Client
from apps.authentication.models import User
from apps.jobs.models import Job
from apps.apply.models import Apply
from django.urls import reverse

from apps.profiles.models import Employee


class ApplicationViewTests(TestCase):

    def setUp(self):
        self.user_company = User.objects.create_user(username='test_company', 
        email='test_company@gmail.com', password='userpass123', is_company=True)
        self.user_employee = User.objects.create_user(username='test_employee', 
        email='test_employee@gmail.com', password='userpass123', is_company=False)
        self.user_employee.employee.set_fields_to_test()

        self.test_job_application_create = Job.objects.create(title='test_job_application_create', salary="a1", description='test',
        scholarship="3", company=self.user_company.company)
        self.test_job_for_application_update = Job.objects.create(title='test_job_for_application_update', salary="a1", description='test',
        scholarship="3", company=self.user_company.company)
        self.test_application = Apply.objects.create(job=self.test_job_for_application_update, employee=self.user_employee.employee, 
        salary="a1", experience='test')

        self.client = Client()
        self.client.login(email='test_employee@gmail.com', password='userpass123')


    def test_get_method_for_application_creation(self):
        response = self.client.get(reverse('apply', args=(self.test_job_application_create.pk, )))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/apply.html')

    def test_creating_application_with_valid_data(self):
        data = {
            'salary': "1a2",
            'experience': "test",
        }

        self.assertEqual(len(Apply.objects.all()), 1)
        response = self.client.post(reverse('apply', args=(self.test_job_application_create.pk, )), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Apply.objects.all()), 2)

    def test_creating_application_with_invalid_data(self):
        data = {
            'salary': "invalid_data",
            'experience': False,
        }

        response = self.client.post(reverse('apply', args=(self.test_job_application_create.pk, )), data=data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(len(Apply.objects.all()), 1)
        self.assertTemplateUsed(response, 'home/apply.html')

    def test_update_application_with_valid_data(self):
        data = {
            "salary": "3+",
            "experience": "updated"
        }

        response = self.client.post(reverse('update-apply', args=(self.test_application.pk, )), data=data)
        self.test_application.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.test_application.salary, "3+")
        self.assertEqual(self.test_application.experience, "updated")

    def test_update_application_with_invalid_data(self):
        data = {
            "salary": "invalid_data",
            "experience": True,
        }
    
        response = self.client.post(reverse('update-apply', args=(self.test_application.pk, )), data=data)
        self.test_application.refresh_from_db()
        self.assertNotEqual(self.test_application.salary, "invalid_data")
        self.assertEqual(response.status_code, 422)
        self.assertTemplateUsed(response, 'home/apply.html')

    def test_update_application_get_method(self):
        response = self.client.get(reverse('update-apply', args=(self.test_application.pk, )))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/apply.html')

    def test_update_unexisting_application_get_method(self):
        response = self.client.get(reverse('update-apply', args=(4, )))

        self.assertEqual(response.status_code, 302)

    def test_delete_application(self):
        response = self.client.post(reverse('delete-apply', args=(self.test_application.pk, )))
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Apply.objects.all()), 0)

    def test_get_all_user_applications(self):
        response = self.client.get(reverse('employee-applications'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/employee_applications.html')
    
    def test_get_company_all_applications(self):
        self.client.logout()
        self.client.login(email=self.user_company.email, password='userpass123')
        response = self.client.get(reverse('job-applications', args=(self.test_job_for_application_update.pk, )))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/job_applications.html')