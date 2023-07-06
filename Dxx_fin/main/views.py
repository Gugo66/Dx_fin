from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from main.forms import RegisterForm
from django.core.mail import send_mail#

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('main:profile')

    def form_valid(self, form):
        form.save()

        email = form.cleaned_data['email']
        send_mail(
            'Подтверждение регистрации',
            'Добро пожаловать! Ваша регистрация прошла успешно.',
            'gurgentadevosyan@mail.ru',  
            [email],  
            fail_silently=False,
        )

        return redirect(self.success_url)
class WebPasswordResetView(PasswordResetView):
    template_name = 'main/password_reset_email.html'


def index(request):
    return render(request, 'main/index.html')

