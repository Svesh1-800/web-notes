from django.db import models
from django.urls import reverse
from django.utils import timezone

# модель для создания категорий
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.name
# модель для создания аттрибутов заметки
class Note(models.Model):
    title_note = models.CharField('Название', blank=False, default='NoTitle', max_length=150)
    category_note = models.ForeignKey(Category, on_delete= models.CASCADE)
    content_note = models.TextField('Содержание', blank=True)
    date_note = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title_note + ' | ' + self.content_note
