from django.test import TestCase
from django.test.client import Client 
from apps.authentication.models import User
from apps.jobs.models import Job
from django.urls import reverse


class JobViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_company = User.objects.create_user(username='test_company', email='test@gmail.com', 
        password='userpass123', is_company=True)
        self.user_employee = User.objects.create_user(username='test_employee', email='test_employee@gmail.com', 
        password='userpass123')
        self.job = Job.objects.create(title='test_job', salary="a1", description='test',
        scholarship="3", company=self.user_company.company)

        self.client.login(email=self.user_company.email, password='userpass123')

    def test_create_job_post_method_with_valid_data(self):
        data = {
            'title': 'Python Dev',
            'salary': '3+',
            'scholarship': '3',
            'description': 'Python Dev'
        }

        self.assertEqual(len(Job.objects.all()), 1)
        response = self.client.post(reverse('create-job'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Job.objects.all()), 2)

    def test_create_job_post_method_with_invalid_data(self):
        response = self.client.post(reverse('create-job'), data=None)
        self.assertEqual(response.status_code, 422)
        self.assertTemplateUsed(response, 'home/job_form.html')
        self.assertEqual(len(Job.objects.all()), 1)

    def test_create_job_get_method(self):
        response = self.client.get(reverse('create-job'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/job_form.html')

    def test_job_update_post_method_with_valid_data(self):
        data = {
            'title': 'job_updated',
            'description': 'updated',
            'salary': 'a1',
            'scholarship': '3'
        }

        response = self.client.post(reverse('update-job', args=(self.job.pk, )), data=data)
        self.job.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.job.title, 'job_updated')
        self.assertEqual(self.job.description, 'updated')

    def test_job_update_post_method_with_invalid_data(self):
        response = self.client.post(reverse('update-job', args=(self.job.pk, )), data=None)
        self.assertEqual(response.status_code, 422)
        self.assertTemplateUsed(response, 'home/job_form.html')

    def test_job_update_get_method(self):
        response = self.client.get(reverse('update-job', args=(self.job.pk, )))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/job_form.html')

    def test_job_delete(self):
        self.job.closed = True
        self.job.save()
        response = self.client.post(reverse('delete-job', args=(self.job.pk, )))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Job.objects.all()), 0)
        self.assertNotIn(self.job, Job.objects.all())

    def test_job_close(self):
        response = self.client.post(reverse('close-job', args=(self.job.pk, )))

        self.job.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.job.closed)

    def test_job_open(self):
        self.job.closed = True
        self.job.save()

        response = self.client.post(reverse('open-job', args=(self.job.pk, )))
        self.job.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.job.closed)

    def test_get_total_company_jobs(self):
        response = self.client.get(reverse('company-jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/company_jobs.html')

    def test_get_employee_total_jobs(self):
        self.client.logout()
        self.client.login(email=self.user_employee.email, password='userpass123')

        response = self.client.get(reverse('employee-jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/all_jobs.html')
        
    def test_search_job(self):
        response = self.client.get(reverse('search-job'), data={'job_title': 'tes'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/search_job.html')
        self.assertEqual(len(response.context['job_qs'].all()), 1)
