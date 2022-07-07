# built-in django imports;
from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model;
class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']