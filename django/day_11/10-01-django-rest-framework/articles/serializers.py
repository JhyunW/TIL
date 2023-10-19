from rest_framework import serializers
from .models import Article, Comment  # 코멘트 모델을 만들기 위해 등록

# ModelForm이 하는 일 : Model 정보를 토대로, 사용자에게 Model과 관련된 어떠한 정보를 보여줌
                        # 혹은 해당 Model의 인스턴스 정보를 생성, 수정 할 수 있게 해줌
#Modelserializer가 하는 일 : Model 정보를 토대로, 사용자에게 Model과 관련된 어떠한 정보
                            # 혹은 해당 model의 인스턴스 정보를 생성, 수정 할 수 있게 해줌.

# 필요한 필드만 조회 필요한 테이블을 필요한 값만 넣어 만듦
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )


# 단일 조회 테이블 만듦 모든 메뉴 넣어서
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
