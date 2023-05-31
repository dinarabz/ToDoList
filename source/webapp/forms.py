from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator
from webapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('summary', 'author', 'description', 'status', 'tags')
        labels = {
            'summary': 'Заголовок статьи',
            'author': 'Автор',
            'description': 'Текст',
            'status': 'Статус',
            'tags': 'Теги'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должно быть длинее 2 символов')
        if Article.objects.filter(title=title).exists():
            raise ValidationError('Заголовок с таким именем уже существует')
        return title
