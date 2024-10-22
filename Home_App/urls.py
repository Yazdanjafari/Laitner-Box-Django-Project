from django.urls import path
from . import views

app_name = "Home_App"

urlpatterns = [
    path("", views.index_show, name="index"),
    path("about", views.about_show, name="about"),
]
