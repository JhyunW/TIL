from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),
    # article/숫자_pk/ 식으로 주소 받음 디테일로
    path('articles/<int:article_pk>/', views.article_detail),  # int:article_pk가 뭐더라
    path('comments/', views.comment_list),
    
]
