from django.shortcuts import render

# Create your views here.
def books(request):
    book_list = [
        {'author': '김시습', 'book_list': ['금오신화', '이생규장전', '만복자서포기']}, 
        {'author': '허균', 'book_list': ['홍길동전', '장생전', '도문대작']},  
        {'author': '남영로', 'book_list': ['옥루몽', '옥련몽']}, 
        {'author': '작자 미상', 'book_list': ['장화홍련전', '가락국 신화', '온달 설화']}, 
        {'author': '임제', 'book_list': ['수성지', '백호집', '원생몽유록']}
]
    context = {   # 여기 대충 어캐 돌아가는거지?.. 파이썬 실행해보기
        'book_list' : book_list
    }
    return render(request, 'books/books.html', context)

def author(request, author_name):
    context = {
        'author_name' : author_name
    }
    return render(request, 'books/author.html', context)
