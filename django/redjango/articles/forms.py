from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('title', 'content')  # 타이틀만 출력
        # exclude = ('user')  # 유저만 제외