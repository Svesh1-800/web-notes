from django.db import models

# модель для создания аттрибутов заметки
class Note(models.Model):
    title_note = models.CharField(blank=False, default='NoTitle',max_length=150)
    category_note = models.CharField(blank=True, default='out', max_length=150)
    content_body = models.CharField(blank=True, max_length=1000)
    post_date_note = models.DateField(auto_now_add=True)
