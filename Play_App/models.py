from django.db import models
from customauth.models import MyUser

class Word(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="کاربر")
    front_word = models.CharField(max_length=55, verbose_name="کلمه رو")
    back_word = models.CharField(max_length=55, verbose_name="کلمه پشت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    
    class Meta:
        verbose_name_plural = "کلمات"
        