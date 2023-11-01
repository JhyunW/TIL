from django.shortcuts import render,redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.

def main(request):
    # 게시글 전체 정보를 조회
    # Model.manager.querySetAPI
    # SELECT * FROM articles_article;
    # articles = Article.objects.all()


    # SELECT * FROM articles_article ORDER BY pk DESC
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles': articles
    }
    # BASE_DIR/articles/templates/articles/main.html
    return render(request,
                  'articles/main.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 물론 생성이 되지는 않는다.
            # form.save() 메서드는 생성된 데이터 인스턴스 반환
            # database의 테이블에 생성될 값 INSERT INTO
            # 이때, article이 가지고 있어야할 user_id를 안넣고 생성할려고 하니 문제생김
            # 그럼 article에 user정보(요청한 유저) 정보를 담아야 하니까
            # 일단 article 생성은 하는데.. db에는 보내지 말자.
            article = form.save(commit = False)
            # 생성된 article 객체의 user속성에 요청보낸 request.user 정보를 담자
            # 담은것은 python의 aritlce변수의 값에만 할당 한것
            # db에 반영
            article.user = request.user
            article.save()
            return redirect('main')
    # 게시글 생성을 위한 form이 필요하네?..
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    # SELECT * FROM articles_article WHERE id = aritlce_pk;
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_pk)
        # DELETE FROM articles_article WHERE pk = article_pk;
        article.delete()
    return redirect('main')

def likes(request, article_pk):
    # 특정 게시글과 요청 보낸 유저의 M:N관계를 생성
    article = Article.objects.get(pk=article_pk)

    # 이미 request.user와 article이 M:N관계를 맺고 있는 상태일 때,
    if request.user in article.like_users.all():
        # 이미 관계를 맺고 있는 상태에서 온 M:N 관계 관련 요청
        # 관계 해제 요청
        article.like_users.remove(request.user)
    # 아닐때
    else:
        # 관계 성립 요청
        article.like_users.add(request.user)
    return redirect('main')

    # 아닐때
