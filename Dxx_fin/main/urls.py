from django.urls import path
from .views import *


app_name = "main"

urlpatterns = [
    path('index', index, name="index"),
    path('profile', profile_view, name="profile"),
    path('', RegisterView.as_view(), name="register"),
    path("password_reset/", WebPasswordResetView.as_view(), name="password_reset"),


]
