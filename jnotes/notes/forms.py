from django import forms
from django.db import models

from .models import Note, Category


# добавляем временное поле, чтобы при выборе категории был не селектор, а простое поле для ввода
class CreateForm(forms.Form):
    title = forms.CharField(max_length=150, required=False, label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'post-title inputs'}))
    category = forms.CharField(max_length=150, required=False, label='Категория',
                               widget=forms.TextInput(attrs={'class': 'post-category inputs'}))
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'post-content inputs'}))

    def clean_title(self):
        if not self.cleaned_data['title']:
            self.cleaned_data['title'] = 'NoTitle'
        return self.cleaned_data['title']

    def clean_category(self):
        if not self.cleaned_data['category']:
            self.cleaned_data['category'] = 'void'
        return self.cleaned_data['category']
