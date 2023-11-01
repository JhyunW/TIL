from django.db import models
from django.conf import settings

# Create your models here.
# python 문법만으로도 편하게 DataBase를 조작하기 위해서 model을 제공한다.
class Article(models.Model):  # 쉽게 생각해서 모델에서 만들어줄것이니까 models.Model불러온다
    # 제목, 내용, 작성시간, 수정시간
    # models 라는 모듈에는 다양한 필드가 정의 되어 있다.
    # 각 필드들은 데이터베이스에 생성될 table의 컬럼별 데이터 타입을 적절하게 정의해 준다.
        # dabase_sometabble
        # | pk | title | content | create_at ....
        # | INT | VARCHAR(100) | TEXT | DATETIME  # 다음 시험 연습으로 적어보기
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 작성 시간 : 사용자가 직접입력 x
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 시간
    updated_at = models.DateTimeField(auto_now=True)
    # User와의 관계 = 1:N
    # article.user (작성자 정보)
    # user = models.ForeignKey('accounts.User')  # 포링키가 뭐야?..
    # user.article_set.all -> 나를 참조하고있는 게시글 모두 조회
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE )  # 위에랑 똑같음, 삭제했을때 공간도 같이 삭제
    # 작성자 = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE )
    
    # user와의 관계 - M:N
    # 좋아요 기능 구현을 위한 관계
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='like_articles')
    # 좋아요누른유저들 = models.ManyToManyField(settings.AUTH_USER_MODEL,
    #                                     relaterd_name='like_articles')
    # related_name 속성이 하는 일
    # a1 게시글 하나는 직접적으로 like_users라는 값을 가지고 있고
    # user1(게시글과 M:N관계를 맺고 있는 유저는) class에 해당 관계에 대한
        # 변수 및 속성 정의한 적 없음
        # 그래서 django가 manager라고 하는 것을 만들어 줌
        # related manager -> user1.article_set.querySET
        # related manager 이름 작성 규칙은 : 관계 맺고 있는 class 의 소문자_set
    # related manager는 M:N만 있는게 아니라, (M:N은 서로가 1:N하고 있는 것)

# 중개 모델을 사용해서 N:M을 표현 할 수 도 있다.
# 중개모델 사용시, User -> like_system -> Article
# articles = User.likesystem_set.all() -> 특정 게시글
    # for article in articles:
    # article.title
class like_system(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




    #=================================================