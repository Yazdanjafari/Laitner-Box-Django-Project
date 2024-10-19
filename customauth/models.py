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
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True, verbose_name="phone number")

    # Personal details
    first_name = models.CharField(max_length=50, verbose_name="نام", help_text="این فیلد باید به فارسی وارد شود")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی", help_text="این فیلد باید به فارسی وارد شود")
    father_name = models.CharField(max_length=50, verbose_name="نام پدر", help_text="این فیلد باید به فارسی وارد شود", blank=True, null=True)
    gender = models.CharField(max_length=50, choices=[('Man', 'آقا'), ('Woman', 'خانم')],  null=True, blank=True, verbose_name="جنسیت")
    date_of_birth = jmodels.jDateField(null=True, blank=True, verbose_name="تاریخ تولد")
    nationality_id = models.CharField(max_length=10, verbose_name="شماره ملی")
    email = models.EmailField(unique=True, blank=True, null=True, verbose_name="ایمیل")
    home_phone = models.CharField(max_length=11, null=True, blank=True, help_text="با پیش شماره (مثال 02155667788)" , verbose_name="شماره منزل")
    
    # Additional User Information
    bio = models.TextField(max_length=500, blank=True, verbose_name="بایوگرافی")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="تصویر پروفایل")

    # Contact and Address Information
    country = models.CharField(max_length=50, blank=True, null=True, default="Iran", verbose_name="کشور", help_text="این فیلد باید به فارسی وارد شود")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="استان", help_text="این فیلد باید به فارسی وارد شود")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="شهر", help_text="این فیلد باید به فارسی وارد شود")
    address = models.TextField(max_length=500, blank=True, null=True, verbose_name="آدرس", help_text="این فیلد باید به فارسی وارد شود")
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="کد پستی")
    
    # Authentication and status flags
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_staff = models.BooleanField(default=False, verbose_name="کارمند")
    is_superuser = models.BooleanField(default=False, verbose_name="ادمین")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="تاریخ پیوستن")
    
    # Account-related flags
    last_login = models.DateTimeField(blank=True, null=True, verbose_name="آخرین ورود")
    email_verified = models.BooleanField(default=False, verbose_name="ایمیل تایید شده")
    phone_verified = models.BooleanField(default=False, verbose_name="تلفن تایید شده")
    
    # Account recovery details
    password_reset_token = models.CharField(max_length=100, blank=True, null=True, verbose_name="توکن بازنشانی رمز عبور")
    password_reset_expiry = models.DateTimeField(blank=True, null=True, verbose_name="انقضای توکن")

    # Marketing preferences
    receive_marketing_emails = models.BooleanField(default=False, verbose_name="دریافت ایمیل های تبلیغاتی")
    receive_sms_notifications = models.BooleanField(default=False, verbose_name="دریافت اعلان های پیامکی")

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'nationality_id']

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.phone_number})'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = "حساب های کاربری"