# import json # 내장 모듈

# # json 데이터
# json_data = '''
# {
#     "name" : "나나나",
#     "age" : "23",
#     "hobbies" : [
#         "공부하기",
#         "음악듣기"
#     ]
# }
# '''

# data = json.loads(json_data)
# print(data)


API_key = '27dabc95e59303def4abeab9a291cd2e'
city_name = "Seoul ,KR"
url = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
import requests
# API 요청 보내기
response = requests.get(url).json()
response
temp = response['main']['temp']
temp