from django.contrib import admin
from .models import Word

@admin.register(Word)
class chef_show (admin.ModelAdmin):
    list_display = ("id", "user", "front_word", "back_word", "day", "box", "created_at", "updated_at", "last_reviewed", "lock_time")
    list_filter = ["user"]
