from django.contrib.auth.forms import UserCreationForm  # 유저 생성(가입) 폼
from django.contrib.auth import get_user_model  # 모델을 만들때 유저 모델을 가져오기 위한 함수

class CustomUserCreationForm(UserCreationForm):  # 새로운 공간에 폼 가져오기
    class Meta(UserCreationForm.Meta):  # 메타에도 유저 크레이션 폼.Meta를 상속해야함
        model = get_user_model()