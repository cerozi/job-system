from django.urls import path
from .views import profile_view, register, login, logout

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]