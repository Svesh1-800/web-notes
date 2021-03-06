# Generated by Django 3.1.5 on 2021-01-25 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_note', models.CharField(blank=True, max_length=150, verbose_name='Название')),
                ('content_note', models.TextField(blank=True, verbose_name='Содержание')),
                ('date_note', models.DateTimeField(auto_now_add=True)),
                ('category_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.category')),
            ],
        ),
    ]
