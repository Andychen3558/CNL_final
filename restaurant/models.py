from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=20)
	# # 座位數
	# site_number = models.IntegerField(default=0)
	# # 進來時間
	# coming_time = models.DurationField()
	# # 跳號機率
	# skip_probability = models.FloatField(default=0.0)
	# # 過號時間限制
	# timeout = models.DurationField()
	# # 預計吃多久
	# eat_time = models.DurationField()
	# # 排隊號碼
	# queue_number = ArrayField(
	# 					models.IntegerField(),
	# 					size=8,
	# 					)
	# # 排隊電話
	# qurue_phone_number = ArrayField(
	# 						models.CharField(max_length=20, blank=True),
	# 						size=8,
	# 					)
	def __str__(self):
		return self.name