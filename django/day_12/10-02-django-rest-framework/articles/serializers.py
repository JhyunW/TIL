from rest_framework import serializers
from .models import Article, Comment

# 댓글 만들거나 상세내용을 확인하거나 할때 필요한 정보 만들어주는애
    # 댓글 만들때, Article에 대한 정보도 필요
        # 하지만 사용자가 입력하지 않음.
    # 댓글 조회시, Article에 대한 정보 필요
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

    # override
    # article이라는 변수는?
        # class Comment에 작성했던 article변수에 해당하는 내용
        # foelds에 작성될 article의 역할을 바꿔줌
    # article = ArticleTitleSerializer(read_only=True)


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)



class ArticleSerializer(serializers.ModelSerializer):
    # 나를 참조하고 있는 모든 댓글 정보 다 가져 오겠다.
        # serializer의 목적 : 가지고 온 데이터를 사용자에게
                                # 어떻게 보여줄것인가 정의
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

