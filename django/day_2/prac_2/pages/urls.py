# pages
from django.urls import path, include  # 장고 폴더안에 urls폴더 안에 패스 폴더 안에 include가 있다
from . import views  # 현재폴더의 views 에서 받아오기

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index')
]
