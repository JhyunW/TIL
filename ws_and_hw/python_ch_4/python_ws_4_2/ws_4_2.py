# ws_4_2.py
import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
for i in range(10):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i+1}'
# API 요청
    response = requests.get(API_URL)
# JSON -> dict 데이터 변환
    parsed_data = response.json()

# 특정 데이터 출력
    print(parsed_data['name'])