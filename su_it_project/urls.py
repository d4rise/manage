# su_it_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # для картинок и медиафайлов

urlpatterns = [
    path('admin/', admin.site.urls),
    # Главная страница (пустая строка '') будет обрабатываться приложением courses
    path('', include('courses.urls')),
    path('auth/', include('users.urls')),
]

# Настройка для того, чтобы аватарки и картинки курсов (MEDIA_ROOT) отдавались во время разработки
# БЕЗ ЭТОГО КАРТИНКИ НЕ БУДУТ РАБОТАТЬ!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)