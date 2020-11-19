from django.urls import path
from .views import HomeView, NoteDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
]
