from django.urls import path
from .views import HomeView, NoteDetailView, NoteAddView, NoteDeleteView, NoteUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('add_note/', NoteAddView.as_view(), name='note-add'),
    path('note/<int:pk>/remove', NoteDeleteView.as_view(), name='note-delete'),
    path('note/<int:pk>/update', NoteUpdateView.as_view(), name='note-update'),
]
