# built-in django imports;
from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model;
class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    email = models.EmailField(('email address'), unique=True)

    def is_company_or_employee(self):
        if self.is_company:
            return 'company'
        return 'employee'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']