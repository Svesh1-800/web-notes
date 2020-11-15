from django.shortcuts import render
from django.views.generic import ListView

from .models import Note

class HomeView(ListView):
    model = Note
    template_name = 'home.html'
    ordering = ['-post_date_note']