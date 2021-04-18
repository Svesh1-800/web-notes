from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic import CreateView, DeleteView, View
from django.urls import reverse_lazy

from .models import Note, Category
from .forms import CreateForm


# вывод шаблона для донатов
class DonationPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='notes/donation.html')


# основная страница, со всеми заметками
class HomeView(ListView):
    model = Note
    template_name = 'notes/home.html'
    ordering = ['-date_note']
    context_object_name = 'notes_list'


# содержание заметки
class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note-detail.html'
    context_object_name = 'note'


# создание заметки
class NoteAddView(CreateView):
    model = Note
    template_name = 'notes/note-add.html'
    form_class = CreateForm


# удаление заметки
class NoteDeleteView(DeleteView):
    model = Note

    success_url = reverse_lazy('notes:home')
    context_object_name = 'note'

    # чтобы удалить заметку сразу, без перехода на другой шаблон
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# Обновление заметки
class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'notes/note-update.html'
    form_class = CreateForm


# вывод всех существующих категорий в блоке "все категории"
class CategoriesList(View):
    def get(self, request, *args, **kwargs):
        for item in Category.objects.all():  # цикл удаляет категории у которых нет записей
            if len(Note.objects.filter(category_note_id=item.pk)) == 0:
                Category.objects.get(name=item).delete()
        model = Category.objects.order_by('name')

        return render(request, 'notes/categories_list.html', {'categories': model})


# вывод все существующих заметок выбранной категории
class OneCategoryList(View):
    def get(self, request, choice):
        category_posts = Note.objects.filter(category_note=choice)
        return render(request, 'notes/home.html', {'notes_list': category_posts})

# order_by() - отсортировать по определенному полю
# values(name) - получить  объекты одного поля
# values_list(name) - получить все объекты одного поля в формате листа
