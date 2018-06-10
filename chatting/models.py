from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Box(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=100)
    chatting_url = models.CharField(max_length=100,default='')
    latitude = models.CharField(max_length=30,default='0')
    longtitude = models.CharField(max_length=30,default='0')
    user = models.ManyToManyField(User)
