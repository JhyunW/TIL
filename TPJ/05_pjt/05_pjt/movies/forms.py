# 폼의 탬플릿을 만드는곳
from django import forms  # 모델쓴것을 기반으로 가져오는 임포트
from .models import Movie, Comment  # 함수?..

class MovieForm(forms.ModelForm):
    class Meta:  # 규칙
        model = Movie
        exclude = ('user',)  
        widgets = {
            'genre': forms.Select(choices=Movie.GENRE_CHOICES)
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
