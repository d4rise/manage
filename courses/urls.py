# courses/urls.py
from django.urls import path
from .views import CourseListView, CourseDetailView, enroll_course, my_courses

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    
    # Страница одного курса (например: /course/1/)
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    
    # Действие записи на курс
    path('course/<int:pk>/enroll/', enroll_course, name='enroll_course'),
    
    # Список моих курсов
    path('my-courses/', my_courses, name='my_courses'),
]
