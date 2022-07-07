# built-in django imports;
from django.test import TestCase

# other apps imports;
from apps.apply.forms import ApplyForm

class ApplicationFormsTest(TestCase):

    def test_form_with_valid_data(self):
        ''' Tests application form with valid data. '''

        form = ApplyForm(data={
            'salary': '3+',
            'experience': 'test'
        })

        self.assertTrue(form.is_valid())

    def test_form_with_unvalid_data(self):
        ''' Tests application form with invalid data. '''

        form = ApplyForm(data=None)

        self.assertFalse(form.is_valid())