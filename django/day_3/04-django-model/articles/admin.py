from django.contrib import admin
# 명시적 상대경로
from .models import Article
# Register your models here.
# admin site에 등록(register)
admin.site.register(Article)