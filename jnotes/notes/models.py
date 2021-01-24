from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


# модель для создания категорий
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, editable=True)

    # метод возвращает строковое представление
    def __str__(self):
        return self.name

    # Метод, который переводит все в нижний регистр.
    # Теперь не имеет значения, в каком регистре все вводится
    # так же убираю тире, чтобы не было проблем со слагами
    def clean(self):
        self.name = (self.name).lower()


# модель для создания аттрибутов заметки
class Note(models.Model):
    title_note = models.CharField('Название', blank=True, max_length=150)
    category_note = models.ForeignKey(Category, on_delete=models.CASCADE)
    content_note = models.TextField('Содержание', blank=True)
    date_note = models.DateTimeField(auto_now_add=True)

    # функция позволяет обработать введенные данные 
    def clean(self):
        if (self.title_note).strip() == "":
            self.title_note = "NoTitle"
    # при создании заметки пользователя перекидывает на главную страничку
    def get_absolute_url(self):
        return reverse('notes:home')

    # строковое представление
    def __str__(self):
        return self.title_note + ' | ' + self.content_note
