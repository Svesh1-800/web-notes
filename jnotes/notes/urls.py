from django.urls import path

from .views import HomeView, NoteDetailView, NoteAddView, NoteDeleteView, NoteUpdateView
from .views import CategoriesList, OneCategoryList
from .views import DonationPageView

from .views import RegisterView,LoginView, LogoutView, test

# устанавливаем пространство имени приложения( но мы выбрали дефолтное значение, могли и не менять)
# выходит, чтобы обратиться к шаблоного данного приложения нужно обращаться через notes:
app_name = 'notes'

# маршрутизатор
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('add_note/', NoteAddView.as_view(), name='note-add'),
    path('note/<int:pk>/remove', NoteDeleteView.as_view(), name='note-delete'),
    path('note/<int:pk>/update', NoteUpdateView.as_view(), name='note-update'),
    path('categories/', CategoriesList.as_view(), name='categories-view'),
    path('category/<int:choice>', OneCategoryList.as_view(), name='one-category'),
    path('donation/', DonationPageView.as_view(), name='donation'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('',test, name='checking'),


]
# as_view() используюется, если мы используем базовые view из generic'a
