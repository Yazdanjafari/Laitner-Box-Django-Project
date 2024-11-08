from django.contrib import admin
from .models import Word

@admin.register(Word)
class chef_show (admin.ModelAdmin):
    list_display = ("id", "user", "front_word", "back_word", "created_at")

