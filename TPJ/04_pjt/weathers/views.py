from django.shortcuts import render
import pandas as pd  # pandas임포트

# Create your views here.
csv_path = 'weathers/data/austin_weather.csv'  # csv파일 불러오기

def problem1(request):
    # 다운로드 받은 데이터 .scv를 pandas DataFrame 형식으로 저장 및 problem1.html 렌더링
    df = pd.read_csv(csv_path)  # df 라는곳에 불러와서 저장후
    context = {
        'df' : df,  # 불러온 항목을 context에 저장
    }
    return render(request, 'problem1.html', context)

def problem2(request):
    # 일 별 온도 비교를 위한 라인 그래프 생성 및 problem2.html 렌더링
    return render(request, 'problem2.html')

def problem3(request):
    # 월 별 온도 비교를 위한 라인 그래프 생성 및 ;;
    return render(request, 'problem3.html')

def problem4(request):
    # 기상 현상 발생 횟수 히스토그램 생성및 ;;
    return render(request, 'problem4.html')