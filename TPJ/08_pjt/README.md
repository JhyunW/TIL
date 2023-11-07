### 알고리즘 구현 및 성능 측정
## A번. CSV 데이터를 DATAFrame으로 변환 후 반환
  1. views.py에 import pandas as pd 를 넣어 판다스 사용준비
  2. 함수를 선언후 변수 = pd.read_csv('CSV파일 주소', encoding='cp949') 로 넣어줌
  3. data = df.to_dict('records') => 데이터라는 변수에 판다스를 사용하여 데이터를 파이썬 딕셔너리 형식으로 변환후 'records'로 데이터를 레코드 단위로 변환하는 옵션으로 각 레코드가 딕셔너리로 변환됨.
  4. return JsonResponse({'data' : data}) => 로 반환

## B번. 결측치 처리 후 데이터 반환
  - 해당하는 명령어 사용
  1. usecols=['가져올키값'] 을 입력해서 원하는 열만 가져오기 가능
  2. nrows=10 로 처음기준으로 필요한 열의 갯수만큼 불러오기
  3. df(변수)["키이름"].value_counts() 중복되는 키가 각 몇개인지 반환
  4. df(변수)["키이름"].value_counts(normalize=True) 분포를 비율로 확인 가능
  5. df['이름'] = df['이름'].astype(str) 로 데이터 타입 변경 가능 여러가지를 한번에 할려면 딕셔너리 이용.
  ex)df = df.astype({'성별': 'category', '직업': 'str'})
  6. 비어있는 값은 NaN(Not a Number)로 나옴
  7. `isna` 의 경우 결측값(NaN)이면 `True` 반환, 정상값이면 `False` 를 반환. => 누락값 구하기에 씀 df.isna().sum()
  +tip. isnull() = isna()
  df.isna().sum(axis=1) 각 행별로 누락된 값 구하기 axis=1 +> 트루
  df.dropna(axis=0, inplace=True) => 각행별 Fals인곳 True로 변경
  df.dropna(axis=0, how='all', inplace=True) => 순서대로 해석하자면 axis=0 각 행방향으로 결측값 제거하되, how='all' 행에 모든 결측값인 경우에만
  df['직업'].fillna('무직', inplace=True) => 빈칸을 해당 값으로 채워줌
  8. `notna` 의 경우 결측값(NaN)이면 `False` 반환, 정상값이면 `True` 를 반환한다.


## C번. 평균나이와 비슷한 10명
  1. age = df['컬럼이름'].mean() 으로 나이의 평균수치 구하기
  2. df['새로운컬럼이름'] = abs(df['컬럼이름'] - age).sort_values() 으로 평균과 나이의 차이 절대값구하기
  3. df = df.sort_values(by=['나이차']) sort_value로 나이차 정렬
  4. df_same = df.head(10) 새로운 변수에 차이차로 순서대로10개 정렬
  5. df_same.drop(columns=['나이차'], inplace=True) 필요없는 컬럼 드랍

## D번. 성능 측정
  1. 새로운 터미널 창에 locust -f ./locust_test.py 입력
  2. 주소로 들어간 후 0.0.0.0 을 지우고 localhost입력
  3. 순서대로 몇명의 유저가, 동시접속유저수, 받을주소(http://localhost:8000/)
  4. 총 접속자: 5000, 동시 접속자: 200, 평균RPS:40.3,응답 시간:93
  4. 총 접속자: 8000, 동시 접속자: 200, 평균RPS:488.5,응답 시간:10558