## 시작시
 1. python -m venv venv
 2. source venv/Scripts/active
 3. pip install -r requirements.txt
 4. .gitognore
 5. django-admin startproject 파일이름 .
 6. python manage.py startapp 앱이름
 7. setting에 앱 추가
 잊지말기


## 긱 URL, View, Templates 에 알맞게 파일 생성
 1. 프로젝트의 urls.py 에서
 ```python
  path("weathers/", include("weathers.urls")),  
 ```
를 추가해 앱으로 url을 연결해줌.
즉 whathers로 오는 주소는 werathwer안에서 받겠다는 뜻
```python
from . import views

urlpatterns = [
    path('problem1/', views.problem1, name='problem1'),
    path('problem2/', views.problem2, name='problem2'),
    path('problem3/', views.problem3, name='problem3'),
    path('problem4/', views.problem4, name='problem4'),
    
    ]
```
  임포트로 현재 폴더의 views를 받아오고.
  위의 프로젝트에서 weathwers로 바로 연결하기로 하였으니 여기서 주소 problem1을 받으면
  views에 있는 problem1함수를 불러오고 이것의 이름은 problem1로 지정하겠다(나중에 url태그로
  불러오기 편하게 하기 위함.)



 2. Views.py에서
 ```python
 def problem1(request):
    # 다운로드 받은 데이터 .scv를 pandas DataFrame 형식으로 저장 및 problem1.html 렌더링
    context = {
      # 리턴 받을 내용
    }
    return render(request, 'problem1.html', context)
 ```
  식으로 함수를 추가 request를 받고  problem.html(주소)에 반환하겠다. context에 들어간 내용들을
    
 3. html파일 만들기
  템플릿폴더에 base.html을 포함 problem.html들을 생성
  ```html
   <a href="{% url "problem1" %}" >문제1</a>|
  ```
  식으로 a태그로 하이퍼링크를 주고 href에 url태그를 사용하여 연결할 name을 입력, 해당 링크를 클릭시 이동을 원하면 그냥 하면 되지만 이동을 원하지 않고 해당 페이지에 띄우길 원할 시에는 
  ```html
  {% extends "base.html" %}
  ```
  을 이용하여 상속을 받는다. 그럼 base페이지에서 problem1의 내용이 나옴
  추가로 밑에 원하는 콘테스트 즉 이미지 등의 파일을 보여줄 공간을 따로
  ```html
  {% block main %}{% endblock main %} <!--을 이용하여 main이라는 이름의 공간을 따로 주고 나중에 사용할 때에도 problem1 의 html에서 사용이 가능>
  ```

 4. pandas 를 이용하여 캐글에서 받은 파일을 views에서 원하는 함수에 DataFrame으로 읽어오기
 ```python
 import pandas as pd

 # Create your views here.
 csv_path = 'weathers/data/austin_weather.csv'
 ```
 로 pandas를 불러오고, csv_path에 불러올 csv파일의 경로를 가상공간 메인을 기준으로 주소를 입력하여 넣기 
 입력할 함수에
 ```python
 df = pd.read_csv(csv_path)  # df 라는곳에 불러와서 저장후
    context = {
        'df' : df,  # 불러온 항목을 context에 저장
    }
 ```

 그 후 problem1.html 이동하여
  df.columns => 제목들 불러오기
  df.values => 2차원 배열로 날짜와 날씨등을 불러옴
  이것을 for문을 사용하여 출력
  ```html
  <!-- 칼럼스 제목들 -->
  {% for colum in df.columns %}
      <th> {{ colum }} </th>
    {% endfor %}
    ===============================
    <!-- 벨류스 2차원배열 날짜와 시간등 -->
    {% for row in df.values %}
    <tr>
      {% for value in row %}
        <td>{{ value }}</td>
      {% endfor %}
    </tr>
    {% endfor %}
  ```
  # 여기까지가 문제 1번