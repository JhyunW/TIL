from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm, CommentForm
# Create your views here.
# render는 html파일 자체를 여는것, redirect는 뷰 함수를 실행시키는것.
def index(request):
    # 전체 영화 데이터 조회 GET
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)


def create(request):  # 같은거 전체 선택 ctrl+shift+l
    # 영화 데이터 작성 폼 출력
    # 유효성 검증 및 영화 데이터 저장 GET & POST
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)  # 입력을 받은것을 넣어줌 
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect('movies:detail', movie.pk)
    else:
        movie_form = MovieForm()
    
    context = {
        'movie_form' : movie_form
    }
    return render(request, 'movies/create.html', context)


def deatil(request, pk):
    # 단일 영화 데이터 및 댓글 목록 조회
    # 댓글 작성 폼 출력 GET
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }

    return render(request, 'movies/detail.html', context)


def update(request):
    # 영화 데이터 수정 페이지 조회
    # 유효성 검증 및 영화 데이터 수정 GET&POST
    return render(request, 'movies/update.html')


def delete(request):
    # 단일 영화 데이터 삭제 POST
    return render(request, 'movies/delete.html')


def comments_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm(request.POST)
    
    


def comments_delete(request):
    # 단일 댓글 데이터 삭제 POST
    return render(request, 'movies/comments_delete.html')