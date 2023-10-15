from django.shortcuts import render
import random
# Create your views here.
def index(request):
    context = {
        'name' : 'jane',
    }
    # 메인 페이지를 응답
    return render(request, 'articles/index.html', context)  # 호출하겠다, 해당 주소를


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods': foods,  # foods를 부르면 리스트 출력
        'picked':picked,  # picked를 부르면 랜덤 뽑기
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')

def catch (request):
    # 사용자로부터 요청을 받아서
    # 요청에서 사용자 입력 데이터를 찾아
    # context에 저장 후 catch 템플릿에 출력
    # print(request)
    # print(type(request))
    # print(request.GET)
    # 여기까지가 딕셔너리 이므로 파이썬 문법으로 가져오기
    print(request.GET.get('message'))
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)