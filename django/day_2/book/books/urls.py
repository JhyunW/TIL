from django.urls import path  # 장고 폴더안에 urls폴더 안에 패스 폴더 안에 include가 있다
from . import views  # 현재폴더의 views 에서 받아오기

app_name = 'books'
urlpatterns = [
    path('', views.books, name='books'),
    # 작가 이름을 받으면 뷰의 author 참고
    path('<author_name>/', views.author, name='author'),
]
