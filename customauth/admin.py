from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from customauth.models import MyUser

admin.site.site_header = "مدیریت وب ابلیکیشن لایتنر باکس"

class UserCreationForm(forms.ModelForm):
    """A form for creating new users with a repeated password."""
    password1 = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)
    password2 = forms.CharField(label="تکرار رمز عبور", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['phone_number', 'first_name', 'last_name', 'email', 'nationality_id']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمزهای عبور یکسان نیستند")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ['phone_number', 'first_name', 'last_name', 'father_name', 'gender', 'date_of_birth', 'email', 'nationality_id', 'is_active', 'is_staff']


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['phone_number', 'first_name', 'last_name', 'father_name', 'date_of_birth', 'nationality_id', 'country', 'state', 'email', 'is_superuser', 'is_staff', 'is_active',]
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'gender', 'date_of_birth', 'country', 'state', 'city', 'profile_picture', 'email_verified', 'phone_verified']

    fieldsets = [
        (None, {'fields': ['phone_number', 'password']}),
        ('اطلاعات شخصی', {'fields': ['first_name', 'last_name', 'father_name', 'gender', 'date_of_birth', 'nationality_id', 'home_phone', 'email', 'profile_picture', 'bio']}),
        ('اطلاعات تماس', {'fields': ['country', 'state', 'city', 'address', 'postal_code']}),
        ('وضعیت حساب', {'fields': ['is_active', 'is_staff', 'is_superuser']}),
        ('تایید احراز هویت', {'fields': ['email_verified', 'phone_verified']}),
        ('تاریخ های مهم', {'fields': ['last_login', 'date_joined']}),
    ]
    
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['phone_number', 'first_name', 'last_name', 'email', 'nationality_id', 'password1', 'password2'],
        }),
    ]

    search_fields = ['phone_number', 'first_name', 'last_name', 'email', 'nationality_id']
    ordering = ['phone_number']
    filter_horizontal = []


admin.site.register(MyUser, UserAdmin)