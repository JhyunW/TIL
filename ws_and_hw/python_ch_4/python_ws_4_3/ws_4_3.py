# ws_4_3.py

import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
dummy_data = []
for i in range(10):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i+1}'

 # API 요청
    response = requests.get(API_URL)
 # JSON -> dict 데이터 변환
    parsed_data = response.json()

    dummy_data.append({'company' : parsed_data['company']['bs'], 'lat' : parsed_data['address']['geo']['lat'], 'lng' : parsed_data['address']['geo']['lng'], 'name' : parsed_data['name']})

# # 응답 데이터 출력
#     print(response)

# # 변환 데이터 출력
#     print(parsed_data)
# # 변환 데이터의 타입
#     print(type(parsed_data))

# # 특정 데이터 출력
print(dummy_data)