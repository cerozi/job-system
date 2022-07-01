from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('', include('apps.authentication.urls')),
    path('', include('apps.profiles.urls')),
    path('', include('apps.jobs.urls'))
]
