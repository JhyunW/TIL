1. 프로젝트, 앱 생성, 깃 생성 -> 세팅 앱 추가
2. API 키 발급, .env에 저장 *주의* API_KEY="시리얼" 식으로 뛰어쓰기x, ""로 표시
3. 프로젝트의 urls에 include로 앱에 이어지도록 설정 + url 페이지 설정
  urlpatterns(프로젝트) = [
    path("경로/" include("앱.파일)) 
  ]

  urlpatterns(앱) = [
    기능 구현
  ]

4. 뷰 페이지에 필요한 데코레이터, 응답, 렌더 등 함수 적용
5. save_deposit_products 에 API키 받기, url가져와 json으로 변환
6. 세팅에 import environ, import os 추가
env = environ.Env( DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env))
API_KEY = env('API_KEY')
를 입력 후 다시 뷰로 돌아가 API키 함수에 settings.API_KEY 넣기 import 잊지말기
7. 모델에 필요한 클래스와 필드 넣기
8. 다시 뷰로 돌아와서 파일을 불러올때
for li in response.get("result").get("baseList"):식으로 불러와 딕셔너리를 선언하여 그안에 모델 이름과 일치하는 키에 넣어주는 식으로 입력
9. serializer.py를 만들어 모델을 임포트 받아온 후 모델이름serializer클래스에 시리얼라이저스.모델시리얼라이저
클래스 메타:
모델 = 모델이름
필드 = 받아올것
지정해주기 => 나중에 뷰 함수에서 serializer1 = DepositProductsSerializer(data=save_products) 식으로 포장 해주기 해주는이유는 유효성 검사를 위함.
10. 이후 겟, 포스트 구분을 조건문으로 만들어주기


## 어려웠던것들
  - 처음 pk를 이용해 데이터를 받아오는게 항상 pk로만 받아와서 당연히 이번에도 그럴줄 알았는데 get(fin_prdt_cd = li.get("fin_prdt_cd")).pk 식으로 다른 방법으로 데이터를 보고 원하는 값을 받아와야 했던걸 못찾아 힘들었다.
  - 