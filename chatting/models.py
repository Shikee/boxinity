from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Box(models.Model):
	user			= models.ManyToManyField(User)				# 장고에서 기본 제공하는 User 을 참조
	created_at		= models.DateTimeField(auto_now_add=True, null=True)			# 생성 날짜
	title			= models.CharField('TITLE', max_length=50)						# Box 제목
	capacity			= models.IntegerField('CAPACITY')									# 제품 가격
