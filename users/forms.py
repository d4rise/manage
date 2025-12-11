# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# --- 1. Форма для РЕГИСТРАЦИИ (была раньше) ---
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')

# --- 2. Форма для ОБНОВЛЕНИЯ ПРОФИЛЯ (ты её пропустил) ---
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'avatar']