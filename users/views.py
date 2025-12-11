# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # Чтобы пускало только тех, кто вошел
from .forms import CustomUserCreationForm, UserUpdateForm

def register(request):
    """Функция регистрации нового студента"""
    if request.method == 'POST':
        # Если данные пришли (пользователь нажал "Зарегистрироваться")
        # request.FILES нужен обязательно для загрузки картинок!
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Сразу входим в систему под новым пользователем
            login(request, user)
            return redirect('courses:course_list')  # Перенаправляем на главную
    else:
        # Если просто открыли страницу
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
        # Если нажали "Сохранить"
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('users:profile') # Перезагружаем страницу после сохранения
    else:
        # Если просто открыли страницу - заполняем форму текущими данными
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)