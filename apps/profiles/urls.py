# django built-in imports;
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# current app imports;
from .views import profile

urlpatterns = [
    path('profile/', profile, name='profile'),
]

# config for user photo be accessed from the templates;
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
