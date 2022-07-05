from django.test import TestCase
from apps.jobs.forms import JobCreateForm


class JobsFormTests(TestCase):

    def test_job_form_with_valid_data(self):
        form = JobCreateForm(data={
            'title': 'test',
            'salary': '3+',
            'description': 'test',
            'scholarship': '3'
        })

        self.assertTrue(form.is_valid())

    def test_job_form_with_invalid_data(self):
        form = JobCreateForm(data=None)

        self.assertFalse(form.is_valid())
