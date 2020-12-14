# Generated by Django 3.1.3 on 2020-11-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_note_date_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category_note',
            field=models.CharField(default='out', max_length=150, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='note',
            name='content_note',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title_note',
            field=models.CharField(default='NoTitle', max_length=150, verbose_name='Название'),
        ),
    ]