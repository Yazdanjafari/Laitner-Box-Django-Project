from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils import timezone
import django_jalali.db.models as jmodels

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone number is required.')
        
        phone_number = self.normalize_phone_number(phone_number)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(phone_number, password, **extra_fields)

    def normalize_phone_number(self, phone_number):
        return phone_number.strip()

class MyUser(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,11}$',
        message="Phone number must be in the format: '+09123456789'. Up to 11 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=11, unique=True, verbose_name="phone number")
    
    # Personal details
    full_name = models.CharField(max_length=50, verbose_name="نام و نام خانوادگی", help_text="این فیلد باید به فارسی وارد شود")
    gender = models.CharField(max_length=50, null=True, blank=True, verbose_name="جنسیت")
    date_of_birth = jmodels.jDateField(null=True, blank=True, verbose_name="تاریخ تولد")
    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="تصویر پروفایل")
    
    # Contact and Address Information
    country = models.CharField(max_length=50, blank=True, null=True, default="ایران", verbose_name="کشور", help_text="این فیلد باید به فارسی وارد شود")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="استان", help_text="این فیلد باید به فارسی وارد شود")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="شهر", help_text="این فیلد باید به فارسی وارد شود")
    
    # Authentication and status flags
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_staff = models.BooleanField(default=False, verbose_name="کارمند")
    is_superuser = models.BooleanField(default=False, verbose_name="ادمین")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="تاریخ پیوستن")
    
    # Account-related flags
    last_login = models.DateTimeField(blank=True, null=True, verbose_name="آخرین ورود")
    email_verified = models.BooleanField(default=False, verbose_name="ایمیل تایید شده")
    phone_verified = models.BooleanField(default=False, verbose_name="تلفن تایید شده")
    
    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name_plural = "حساب های کاربری"
