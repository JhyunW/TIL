from django import forms
from .models import Article

# class ArticleForm(forms.form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        
        label='제목',
        widget=forms.TextInput(
            attrs = {
                'class': 'my-title'
            }
        )
    )
    # model 등록
    class Meta:
        model = Article
        fields = '__all__'
        # field = ('title')
        # exclude = ('title')