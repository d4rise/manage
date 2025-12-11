# courses/models.py
from django.db import models
from django.conf import settings  # Ссылка на нашу модель User

class Category(models.Model):
    title = models.CharField("Название категории", max_length=100)
    # slug нужен для красивой ссылки (например: /courses/python/)
    slug = models.SlugField(unique=True, verbose_name="URL-метка")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="courses")
    title = models.CharField("Название курса", max_length=200)
    description = models.TextField("Описание курса")
    price = models.DecimalField("Цена (тенге)", max_digits=10, decimal_places=0)
    image = models.ImageField("Картинка курса", upload_to='courses/', null=True, blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    """Таблица записи студента на курс"""
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Студент", related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    enrolled_at = models.DateTimeField("Дата записи", auto_now_add=True)

    class Meta:
        verbose_name = "Запись на курс"
        verbose_name_plural = "Записи на курсы"
        unique_together = ('student', 'course') # Чтобы нельзя было купить один курс дважды

    def __str__(self):
        return f"{self.student} -> {self.course}"