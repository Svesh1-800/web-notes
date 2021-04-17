from django.contrib import admin

from .models import Note, Category


# для отображения полей в админке для модели Note
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_note', 'category_note', 'date_note')
    list_display_links = ('id', 'title_note')  # будут использоваться как ссылки
    search_fields = ('title_note',)  # по этим полям будет осуществляться поиск


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ['name', ]


# регистрация моделей, с которыми мы хотим взаимодействовать в админке
admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)
