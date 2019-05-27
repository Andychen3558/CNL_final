from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SignUpForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
	add_form = SignUpForm
	model = CustomUser
	list_display = ['username', 'phone_number',]

admin.site.register(CustomUser, CustomUserAdmin)