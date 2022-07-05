from django.test import TestCase
from apps.authentication.models import User

class ProfilesModelTests(TestCase):

    def setUp(self):
        self.user_employee = User.objects.create_user(username='test_employee', 
        email='test_employee@gmail.com', password='userpass123', is_company=False)

    def test_check_null_fields(self):
        self.assertIsNone(self.user_employee.employee.check_null_fields())
    
    def test_set_fields_to_test(self):
        self.user_employee.employee.set_fields_to_test()
        self.user_employee.refresh_from_db()
        self.assertEqual(self.user_employee.employee.name, 'test')