from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):  # 영화 제목 필드
    GENRE_CHOICES = (
        ('comedy', 'Comedy'),
        ('fantasy', 'Fantasy'),
        ('romance', 'Romance'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # 영화 제목
    summary = models.TextField()  # 줄거리
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)  # 장르
    rating = models.FloatField()  # 평점


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()  # 댓글 내용