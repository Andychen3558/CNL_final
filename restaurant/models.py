from django.db import models
from datetime import timedelta
from django.conf import settings
# Create your models here.
class Restaurant(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	# created_by = models.ForeignKey(User)
	restaurant_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=20)
	# 座位數
	seat_number = models.IntegerField(default=0)
	# 跳號機率
	skip_probability = models.FloatField(default=0.1)
	# 過號時間限制
	timeout = models.DurationField(default=timedelta(minutes=3))
	# 進來時間
	coming_time = models.TextField(default="")
	# 預計吃多久
	eat_time = models.DurationField(default=timedelta(minutes=30))

	# 排隊資訊	||柯//09||李//02
	waiting_queue = models.TextField(default="")
	# 用餐資訊
	dining_queue = models.TextField(default="")
	# 每位客人用餐時間紀錄 ||name/開始吃飯時間
	dining_time = models.TextField(default="")

	# 平均用餐時間
	dining_time_average = models.FloatField(default=0.0)
	# 總用餐人數
	dining_total_num = models.IntegerField(default=0)

	# 總訂位人數
	reservation_total_num = models.IntegerField(default=0)
	# 跳號人數
	reservation_skip_num = models.IntegerField(default=0)

	def __str__(self):
		return self.restaurant_name

