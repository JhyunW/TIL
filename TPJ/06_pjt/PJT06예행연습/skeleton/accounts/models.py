from django.db import models
# 원래는 주소라서 contrib/auth식으로 갈텐데
# 이건 어떻게 . 을 사용해서 클래스처럼 접근이 가능한가?
# __init__ 덕분.
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):  # 유저라는 클래스를 만들어줌. 앞으로 유저라는 이름들은 이 클래스로 관리
    # 유저네임, 패스워드(암호화,복호화), 관리자, 관계자 등등 해야함
    # 너무 많으니 2번 줄의 import를 받아와서 이걸 사용하자!
    pass