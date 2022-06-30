from django.urls import path
from .views import profile_view, register, login, logout

urlpatterns = [
    path('perfil/', profile_view, name='perfil'),
    path('registrar/', register, name='registrar'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]