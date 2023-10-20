from django.contrib.auth.forms import UserCreationForm

# model 선택 세 가지 방법
# 1. 직접 가져오기 -> 버그확률 있어 권장x
# from .models import User
# 2. settings에 설정된 모델 가져오기
# from django.conf import settings  # model = settings.AUTH_USER_MODEL
# 3. get_user_model 메서드 활용
from django.contrib.auth import get_user_model

# 충돌 방지를 위해 다른이름의 방을 새로 파서 폼을 똑같이 가져옴
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # 사용자가 무엇을 입력할 수 있음 좋을까? 에 대한 작성
        # fields = UserCreationForm.Meta.fields 위에 Meta에서 상속받는것과 동일