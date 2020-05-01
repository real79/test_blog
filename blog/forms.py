from django import forms
from .models import ArticleModel


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'body', 'image']