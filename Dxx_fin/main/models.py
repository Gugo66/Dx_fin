from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
class CustomUser(AbstractUser):
    country = CountryField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
