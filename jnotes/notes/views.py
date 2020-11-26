from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy

from .models import Note

# основная страница, со всеми заметками
class HomeView(ListView):
    model = Note
    template_name = 'home.html'
    ordering = ['-title_note']
    context_object_name = 'notes_list'

# содержание заметки
class NoteDetailView(DetailView):
    model = Note
    template_name = 'note-detail.html'
    context_object_name = 'note'

# создание заметки
class NoteAddView(CreateView):
    model = Note
    template_name = 'add_note.html'
    fields = '__all__'

# удаление заметки
class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note-delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'note'

# Обновление заметки
class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'note-update.html'
    fields = '__all__'


# вывод всех существующих категорий в блоке "все категории"
def CategoriesList(request):
    just_categories = set()
    data = Note.objects.filter().values_list('category_note', flat=True)
    for note in data:
        just_categories.add(note)
    context = {
        'categories': just_categories

    }
    return render(request, 'categories_list.html', context= context)


# values(name) - получить  объекты одного поля
# values_list(name) - получить все объекты одного поля в формате листа



