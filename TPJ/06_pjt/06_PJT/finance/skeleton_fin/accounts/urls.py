
from django.urls import path
from . import views  # 현재 폴더의 뷰 함수 불러오기 위해 설정

# 프로젝트의 urls에서 accounts를 입력 받으면 이곳으로 오도록 설정
app_name = 'accounts'
# 로그인, 로그아웃, 회원가입 url의 행동들
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/follow/', views.follow, name='follow')
]
