from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('auth/', include('apps.authentication.urls')),
    path('', include('apps.profiles.urls')),
    path('', include('apps.jobs.urls')),
    path('', include('apps.apply.urls')),
    path('', include('apps.notifications.urls')),
    path('', include('apps.api.urls'))
]
