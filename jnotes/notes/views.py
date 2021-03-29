from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy


from .models import Note, Category
from .forms import CreateForm


def donation_page(request):
    return render(request=request,template_name='donation.html')

# основная страница, со всеми заметками
class HomeView(ListView):
    model = Note
    template_name = 'home.html'
    ordering = ['-date_note']
    context_object_name = 'notes_list'


# содержание заметки
class NoteDetailView(DetailView):
    model = Note
    template_name = 'note-detail.html'
    context_object_name = 'note'


# создание заметки
class NoteAddView(CreateView):
    model = Note
    template_name = 'note-add.html'
    form_class = CreateForm
    


# удаление заметки
class NoteDeleteView(DeleteView):
    model = Note
    
    success_url = reverse_lazy('notes:home')
    context_object_name = 'note'

    success_message = 'safsadasd'

    # чтобы удалить заметку сразу, без перехода на другой шаблон
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    


# Обновление заметки
class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'note-update.html'
    form_class = CreateForm


# вывод всех существующих категорий в блоке "все категории"
def CategoriesList(request):

    for item in Category.objects.all(): # цикл удаляет категории у которых нет записей
        if len(Note.objects.filter(category_note_id=item.pk))==0:
            Category.objects.get(name=item).delete()
    data2 = Category.objects.order_by('name')

    context = {
        'categories': data2
    }

    return render(request, 'categories_list.html', context=context)


# вывод все существующих заметок выбранной категории
def OneCategoryList(request, choice):
    category_posts = Note.objects.filter(category_note=choice)
    return render(request, 'home.html', {'notes_list': category_posts})



# order_by() - отсортировать по определенному полю
# values(name) - получить  объекты одного поля
# values_list(name) - получить все объекты одного поля в формате листа
