# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Варианты ролей для выбора
    ROLE_CHOICES = (
        ('student', 'Студент'),
        ('director', 'Директор'),
        ('admin', 'Администратор'),
    )

    # Дополнительные поля
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student',
        verbose_name='Роль'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
        verbose_name='Фото профиля'
    )

    # Можно добавить телефон или о себе, если нужно, но пока хватит

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    # Метод для быстрой проверки, директор ли это (понадобится в шаблонах)
    @property
    def is_director(self):
        return self.role == 'director'