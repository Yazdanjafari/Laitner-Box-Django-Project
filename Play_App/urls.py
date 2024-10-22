from django.urls import path
from . import views

app_name = "Play_App"

urlpatterns = [
    path("game", views.game_show, name="game"),
    path("add_word", views.add_word_show, name="add_word"),
]
