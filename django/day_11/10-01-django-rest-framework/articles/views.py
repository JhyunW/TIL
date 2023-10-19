from rest_framework.response import Response
# 오류가 뜰 시에 밑에 데코레이터 추가 사실적으로 필수임
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
# GET에 대한 요청만 통과 / GET과 PST 둘다 받음
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 아티클 오브젝트 모든걸 가져오기
        articles = Article.objects.all()
        # articles에 들어있는 데이터들을 HTML에 그려서 반환
        # articles에 들어있는 데이터들을 JSON으로 변환해서 반환
        # 타입을 변환
        serializer = ArticleListSerializer(articles, many=True)
        # 리스폰스를 이용하여 시리얼라이즈 데이터 추출
        return Response(serializer.data)
    elif request.method == 'POST':
        # 아티클 시리얼라이저 클래스의 데이터를 받아서
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 통과에 성공 했을 때 201번 내보내기
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 생성에 실패 했을때 errors를 사용해서 에러를 출력, 실패코드 400 출력
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
# 응답 받을것과, 아티클의 고유 번호 불러오기
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)  # 고휴 번호 가져오기
    if request.method == 'GET':
        serializer = ArticleSerializer(article)  # 만들어둔 시리얼라이저에서의 클래스
        return Response(serializer.data)
    
    # 딜리트를 받았을 경우
    elif request.method == 'DELETE':
        # 아티클 삭제
        article.delete()
        # 삭제 안내 표시 해보기
        # data = {
        #     'DELETE' : f'{aritlce_pk}번 째 게시글이 정상적으로 삭제 되었습니다.'
        # }
        # 204 삭제했다를 표시
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])  # 데코 꼭 붙이기 약속임
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)