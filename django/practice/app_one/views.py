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