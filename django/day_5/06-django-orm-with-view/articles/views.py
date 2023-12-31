from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)



def detail(request, pk):
    article = Article.objects.get(pk=pk)  # 찾고나서의 결과가 두개이상이면 에러가 남get 특징
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(requeset):
    title = requeset.POST.get('title')
    content = requeset.POST.get('content')
    
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    
    # 2
    article = Article(title=title, content=content)
    article.save()
    
    # 3
    # Article.object.create(title=title, content=content)
    
    return redirect('articles:index')

def delete(request, pk):
    # 몇 번 게시글을 삭제할 것인지 조회
    article = Article.objects.get(pk=pk)
    # 조회한 게시글을 삭제
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/edit.html')

def update(requeset, pk):
    title = requeset.POST.get('title')
    content = requeset.POST.get('content')
    
    # 수정하고자하는 게시글을 조회
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()
    
    return redirect('articles:detail',article.pk)