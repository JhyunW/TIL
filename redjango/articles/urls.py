from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('create/', views.create, name='create'),
    # 사용자가 경로에 작성한 정수를 article_pk 라는 변수에 담아서 쓰겠다.
    path('<int:article_pk', views.detail, name='detail'),
    path('<int:article_pk/delete', views.delete, name='delete'),
    path('<int:article_pk/likes/', views.likes, name='likes')

]