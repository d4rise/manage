
from django.views.generic import ListView
from .models import Course, Category
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Для всплывающих сообщений
from .models import Course, Enrollment, Category
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
        class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Проверяем, записан ли уже пользователь на этот курс
        if self.request.user.is_authenticated:
            context['is_enrolled'] = Enrollment.objects.filter(
                user=self.request.user, 
                course=self.object
            ).exists()
        else:
            context['is_enrolled'] = False
        return context

@login_required # Только для вошедших
def enroll_course(request, pk):
    """Функция записи на курс"""
    course = get_object_or_404(Course, pk=pk)
    
    # Проверяем, не записан ли уже
    already_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    
    if not already_enrolled:
        # Создаем запись
        Enrollment.objects.create(user=request.user, course=course)
        messages.success(request, f'Вы успешно записались на курс {course.title}!')
    else:
        messages.warning(request, 'Вы уже записаны на этот курс.')
        
    return redirect('courses:my_courses')

@login_required
def my_courses(request):
    """Страница 'Мои курсы'"""
    # Получаем все записи текущего пользователя
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})
