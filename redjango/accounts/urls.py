from django.urls import path, include
from . import views

'''
app_name과 pattern_name은 왜 정의해 주는가?
1. 하드코딩을 피하기 위해서 -> 수종사항 발생시 손으로 일일히 다 바꿔주는 일..
'''
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
