from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from datetime import timedelta

# Create your models here.
class CustomUser(AbstractUser):
	phone_regex = RegexValidator(regex=r'^((?=(09))[0-9]{10})$', message="Phone number must be entered in the format: '09xxxxxxxx'")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, help_text='Required. Inform a valid phone number.') # validators should be a list
	#reserve_restaurant = models.ForeignKey(Dicty, db_index=True)
	arrival_time = models.DurationField(null=True, blank=True, default=timedelta(minutes=5),verbose_name='Arrival time')
	
	def __str__(self):
		return self.username