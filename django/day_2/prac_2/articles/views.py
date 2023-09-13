from django.shortcuts import render

# Create your views here.
def  index(request):
    context = {
        'greeting' : '반갑습니다.'
    }
    return render(request, 'articles/index.html', context)  # 리퀘스트, 경로, 콘텍스트

def random_number(request, number):
    next_number = number + 1
    context = {
        'number' : number,
        'next_number' : next_number
    }
    # render 함수의 2번째 인자는 파일 위치 (경로)
    return render(request, 'articles/random_number.html', context)