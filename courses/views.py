# courses/views.py
from django.views.generic import ListView
from .models import Course, Category

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        # Здесь мы позже добавим фильтрацию (Поиск)
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all() # Передаем категории для меню
        return context