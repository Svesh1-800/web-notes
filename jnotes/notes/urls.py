from django.urls import path

from .views import HomeView, NoteDetailView, NoteAddView, NoteDeleteView, NoteUpdateView
from .views import CategoriesList, OneCategoryList
from .views import donation_page

# устанавливаем пространство имени приложения( но мы выбрали дефолтное значение, могли и не менять)
# выходит, чтобы обратиться к шаблоного данного приложения нужно обращаться через notes:
app_name = 'notes'

# маршрутизатор
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('add_note/', NoteAddView.as_view(), name='note-add'),
    path('note/<int:pk>/remove', NoteDeleteView.as_view(), name='note-delete'),
    path('note/<int:pk>/update', NoteUpdateView.as_view(), name='note-update'),
    path('categories/', CategoriesList, name='categories-view'),
    path('category/<int:choice>', OneCategoryList, name='one-category'),
    path('donation/', donation_page, name='donation'),

]
# as_view() используюется, если мы используем базовые view из generic'a
