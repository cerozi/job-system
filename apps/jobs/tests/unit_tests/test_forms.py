# django built-in imports;
from django.test import TestCase

# other apps imports;
from apps.jobs.forms import JobCreateForm


class JobsFormTests(TestCase):
    ''' Tests the forms for the job model. '''

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
