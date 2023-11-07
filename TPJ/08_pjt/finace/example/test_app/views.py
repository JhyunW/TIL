from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import pandas as pd
# A번
def pd_data (request) : 
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')  # 파일 불러서 넣어주기
    # B번 - 비어있는 값을 NULL 문자열로 치환
    df.fillna('NULL', inplace=True)
    data = df.to_dict('records')
    return JsonResponse({'data' : data})

def pd_avg(request) :
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')  # 파일 불러서 넣어주기
    # 평균값과 가장 비슷한 나이인 10개의 행을 새로운 DataFrame으로 만들어 반환
    age = df['나이'].mean()  # 46.2222
    df['나이차'] = abs(df['나이'] - age).sort_values()  # 평균과 나이의 차이 절대값구하기
    df = df.sort_values(by=['나이차'])  # 나이차 내림차순 정렬
    df_same = df.head(10)  # 내림차순 10개 뽑아오기
    df_same.drop(columns=['나이차'], inplace=True)  # 칼럼 드랍
    data = df_same.to_dict('records')
    return JsonResponse({'data' : data})





array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)
