from django.urls import path
from . import views

app_name = "Authentication_App"

urlpatterns = [
    path("signup", views.signup_show, name="signup"),
    path("singup_check", views.singup, name="singup_check"),
    path("login", views.login_show, name="login"),
    path("profile", views.profile_show, name="profile"),
    path('logout', views.Logout_show, name="logout"),
]
