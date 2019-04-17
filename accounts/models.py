from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
# 유저 model customizing

'''
User model을 불러올 때
1. models.py
-> settings.AUTH_USER_MODEL
2. 나머지
-> get_user_model()
'''
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="followings")
  