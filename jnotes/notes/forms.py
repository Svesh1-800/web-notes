from django import forms
from django.db import models

from .models import Note, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))




class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


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
