from django.db import models
from django.urls import reverse

from datetime import datetime


# модель для создания категорий
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, editable=True)

    # метод возвращает строковое представление
    def __str__(self):
        return self.name

    # Метод, который переводит все в нижний регистр.
    # Теперь не имеет значения, в каком регистре все вводится
    def clean(self):
        self.name = self.name.lower()

    # использую класс для того, чтобы преобразовать нужные данные в админке
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


# модель для создания аттрибутов заметки


class Note(models.Model):
    title_note = models.CharField(blank=True, max_length=150, verbose_name='Заголовок')
    category_note = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, verbose_name='категория')
    content_note = models.TextField(blank=True, verbose_name='Контент')
    date_note = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    # функция позволяет обработать введенные данные
    def clean(self):
        if self.title_note.strip() == "":
            self.title_note = "NoTitle"

    def get_absolute_url(self):
        return reverse('notes:home')

    # строковое представление
    def __str__(self):
        formatted_time = datetime.strftime(self.date_note, "%d.%m.%Y")
        formatted_view = self.title_note + '|' + str(self.category_note) + '->' + formatted_time
        return formatted_view

    # использую класс для того, чтобы преобразовать нужные данные в админке
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-date_note']
