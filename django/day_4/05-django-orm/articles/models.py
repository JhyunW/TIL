from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)  # 최대 글자 설정
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 처음 저장값
    update_at = models.DateTimeField(auto_now=True)  # 매번 저장마다 갱신