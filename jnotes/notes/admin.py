from django.contrib import admin

from .models import Note, Category

# регистрация моделей, с которыми мы хотим взаимодействовать в админке
admin.site.register(Note)
admin.site.register(Category)
