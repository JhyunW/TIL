from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('index/', views.index, name='index'),  # 찾아갈 경로, 파일을 찾을위치, 이름
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.deatil, name='detail'),  # 숫자별로 받아오기?
    path('<int:movie_pk>/comments', views.comments_create, name='comments_create'),
]