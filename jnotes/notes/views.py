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

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'note-update.html'
    fields = '__all__'

