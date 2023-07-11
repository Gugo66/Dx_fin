from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from main.models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    country = CountryField()
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2023), empty_label=("Year", "Month", "Day")))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'country', 'birth_date']
