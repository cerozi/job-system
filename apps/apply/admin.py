# built-in django imports;
from django.contrib import admin

# current app imports;
from .models import Apply

admin.site.register(Apply)
