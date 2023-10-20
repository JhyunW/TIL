from django.db import models
from django.contrib.auth.models import AbstractUser  # 유저 필드
# Create your models here.

class User(AbstractUser):  # 유저 필드 불러올때 쓸 클래스
    followings = models.ManyToManyField('self', related_name="following", symmetrical=False)  # 대칭을 지워주기
