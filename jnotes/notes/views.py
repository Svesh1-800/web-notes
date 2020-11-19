from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Note

class HomeView(ListView):
    model = Note
    template_name = 'home.html'
    ordering = ['-post_date_note']
    context_object_name = 'notes_list'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note-detail.html'
    context_object_name = 'note'