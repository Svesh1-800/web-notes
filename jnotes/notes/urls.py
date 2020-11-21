from django.urls import path
from .views import HomeView, NoteDetailView, AddNoteView, NoteDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('add_note/', AddNoteView.as_view(), name='add-note'),
    path('note/<int:pk>/remove', NoteDeleteView.as_view(), name='note-delete'),
]
