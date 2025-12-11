# users/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile
app_name = 'users'

urlpatterns = [
    # Наша самописная регистрация
    path('register/', register, name='register'),

    # Встроенный вход в систему (Login)
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    # Встроенный выход (Logout)
    # next_page='/' означает, что после выхода кинет на главную
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', profile, name='profile'),
]