# Generated by Django 3.1 on 2020-11-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_note', models.CharField(default='NoTitle', max_length=150)),
                ('category_note', models.CharField(blank=True, default='out', max_length=150)),
                ('content_note', models.TextField(blank=True)),
                ('date_note', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
