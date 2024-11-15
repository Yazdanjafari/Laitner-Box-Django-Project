from django.db import models
from customauth.models import MyUser

class Word(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="کاربر")
    front_word = models.CharField(max_length=255, verbose_name="کلمه رو")
    back_word = models.CharField(max_length=255, verbose_name="کلمه پشت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین تغیر")
    last_reviewed = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین بازی")
    box = models.IntegerField(default=1, verbose_name="جعبه")
    day = models.IntegerField(default=1, verbose_name="روز")
    is_correct = models.BooleanField(default=False, verbose_name="تصحیح")
    lock_time = models.DateTimeField(null=True, blank=True, verbose_name="زمان قفل شدن بازی")
    
    def update_box(self):
        if 1 <= self.day <= 1:
            self.box = 1
        elif 2 <= self.day <= 3:
            self.box = 2
        elif 4 <= self.day <= 8:
            self.box = 3
        elif 9 <= self.day <= 15:
            self.box = 4
        elif 16 <= self.day <= 30:
            self.box = 5
        else:
            self.delete()
        self.save()
        
    class Meta:
        verbose_name_plural = "کلمات"
        
      