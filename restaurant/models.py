from django.db import models
from datetime import timedelta
# Create your models here.
class Restaurant(models.Model):
	restaurant_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=20)
	# # 座位數
	seat_number = models.IntegerField(default=0)
	# # 進來時間
	# coming_time = models.DurationField()
	# # 跳號機率
	skip_probability = models.FloatField(default=0.1)
	# # 過號時間限制
	timeout = models.DurationField(default=timedelta(minutes=3))
	# # 預計吃多久
	eat_time = models.DurationField(default=timedelta(minutes=30))
	# # 排隊號碼
	waiting_queue = models.TextField(default="")
	# # 排隊電話
	waiting_phonenumber = models.TextField(default="")
	# 					)
	def __str__(self):
		return self.restaurant_name