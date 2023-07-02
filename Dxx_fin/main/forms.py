from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError
#
# from core.models import Buyer


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):

        fields = UserCreationForm.Meta.fields + ("email", )