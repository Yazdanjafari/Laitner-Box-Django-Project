from django.db import models
from customauth.models import MyUser

class Word(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="کاربر")
    front_word = models.CharField(max_length=255, verbose_name="کلمه رو")
    back_word = models.CharField(max_length=255, verbose_name="کلمه پشت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین تغیر")
    last_reviewed = models.DateField(auto_now=True, verbose_name="تاریخ آخرین بازی")
    box = models.IntegerField(default=1, verbose_name="جعبه")
    day = models.IntegerField(default=1, verbose_name="روز")
    
    class Meta:
        verbose_name_plural = "کلمات"
        