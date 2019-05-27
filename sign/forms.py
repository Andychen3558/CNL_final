from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class SignUpForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^((?=(09))[0-9]{10})$', message="Phone number must be entered in the format: '09xxxxxxxx'")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17, help_text='Required. Inform a valid phone number.') # validators should be a list

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'phone_number')