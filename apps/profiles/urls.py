from django.urls import path
from .views import profile

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', profile, name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)