from django.urls import path
from . import views

app_name = "Authentication_App"

urlpatterns = [
    path("signup", views.signup_show, name="signup"),
    path("login", views.login_show, name="login"),
]
