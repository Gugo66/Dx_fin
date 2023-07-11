from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from main.forms import RegisterForm
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from datetime import date
from datetime import datetime


@login_required
def profile_view(request):
    birth_date = request.user.birth_date  # Извлекаем дату рождения пользователя
    age = calculate_age(birth_date)  # Вычисляем возраст

    country = request.user.country  # Извлекаем выбранную страну

    context = {
        'age': age,
        'country': country
    }

    return render(request, 'main/profile.html', context)





def calculate_age(birth_date):
    today = datetime.now().date()
    age = today.year - birth_date.year

    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    return age

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('main:profile')

    def form_valid(self, form):
        response = super().form_valid(form)

        country = form.cleaned_data['country']
        birth_date = form.cleaned_data['birth_date']

        user = form.save(commit=False)
        user.country = country
        user.birth_date = birth_date
        user.save()

        email = form.cleaned_data['email']
        send_mail(
            'Подтверждение регистрации',
            'Добро пожаловать! Ваша регистрация прошла успешно.',
            'gurgentadevosyan@mail.ru',
            [email],
            fail_silently=False,
        )

        return response



class WebPasswordResetView(PasswordResetView):
    template_name = 'main/password_reset_email.html'


def index(request):
    return render(request, 'main/index.html')

