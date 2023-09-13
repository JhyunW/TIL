import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : 'jane',
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # print(request)
    # print(request.GET)
    # print(request.GET('message'))
    # 사용자로 부터 요청을 받아서
    # 요청에서 사용자 입력 데이터를 찾아
    # context에 저장 후 catch 템플링세 출력
    message = request.GET.get('message')  # request.GET 까지가 딕셔너리, get() 로 가져오기
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)

def greeting(requset, name):  # 받아오는걸 여러개
    context = {
        'name': name,
    }
    return render(requset, 'articles/greeting.html', context)

def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)