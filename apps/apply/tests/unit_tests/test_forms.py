from django.test import TestCase
from apps.apply.forms import ApplyForm

class ApplicationFormsTest(TestCase):

    def test_form_with_valid_data(self):
        form = ApplyForm(data={
            'salary': '3+',
            'experience': 'test'
        })

        self.assertTrue(form.is_valid())

    def test_form_with_unvalid_data(self):
        form = ApplyForm(data=None)

        self.assertFalse(form.is_valid())