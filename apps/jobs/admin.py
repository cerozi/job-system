# django built-in imports;
from django.contrib import admin

# current app imports;
from .models import Job


admin.site.register(Job)