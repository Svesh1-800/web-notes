from django.db import models
from django.urls import reverse

# модель для создания аттрибутов заметки
class Note(models.Model):
    title_note = models.CharField(blank=False, default='NoTitle', max_length=150)
    category_note = models.CharField(blank=True, default='out', max_length=150)
    content_note = models.TextField(blank=True)
    post_date_note = models.TimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title_note + ' | ' + self.content_note
