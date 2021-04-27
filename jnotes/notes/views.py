from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic import CreateView, DeleteView, View
from django.contrib.auth import login, logout
from .models import Note, Category
from django.contrib.auth.models import User
from .forms import CreateForm, UserRegisterForm, UserLoginForm


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('notes:home')


class RegisterView(View):
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'ого вау')
            return redirect('notes:home')
        else:
            messages.error(request, 'бля')
            return render(request, 'notes/register.html', {'form': form})

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'notes/register.html', {'form': form})


class LoginView(View):
    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('notes:home')
        else:
            messages.error(request, 'бля')
            return render(request, 'notes/login.html', {'form': form})

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'notes/login.html', {'form': form})


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

    # paginate_by = 2  это на случай пагинации
    def get_queryset(self):
        if self.request.user.is_active:
            return Note.objects.filter(author=self.request.user).select_related('category_note')


# содержание заметки
class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note-detail.html'
    context_object_name = 'note'


# создание заметки
class NoteAddView(View):
    def post(self, request, *args, **kwargs):
        form = CreateForm(request.POST)
        if form.is_valid():
            chosen_category = Category.objects.get_or_create(name=form.cleaned_data['category'])
            Note.objects.create(title_note=form.cleaned_data['title'],
                                category_note=Category(chosen_category[0]).pk,
                                content_note=form.cleaned_data['content'],
                                author=User(request.user.pk)
                                )

            return redirect('notes:home')

    def get(self, request):
        form = CreateForm()
        return render(request, 'notes/note-add.html', {'form': form})


# удаление заметки
class NoteDeleteView(DeleteView):
    model = Note

    success_url = reverse_lazy('notes:home')

    # чтобы удалить заметку сразу, без перехода на другой шаблон
    def get(self, *args, **kwargs):
        messages.success(self.request, 'ddddd')
        return self.post(*args, **kwargs)


# Обновление заметки
class NoteUpdateView(View):
    def post(self, request, *args, **kwargs):
        form = CreateForm(request.POST)
        if form.is_valid():
            chosen_category = Category.objects.get_or_create(name=form.cleaned_data['category'])
            chosen_note = Note.objects.get(pk=self.kwargs['pk'])
            chosen_note.title_note = form.cleaned_data['title']
            chosen_note.category_note = Category(chosen_category[0]).pk
            chosen_note.content_note = form.cleaned_data['content']
            chosen_note.save()
            return redirect('notes:home')

    def get(self, request, *args, **kwargs):
        chosen_note = Note.objects.get(pk=self.kwargs['pk'])
        data = {
            'title': chosen_note.title_note,
            'category': chosen_note.category_note,
            'content': chosen_note.content_note,
        }
        form = CreateForm(data)
        return render(request, 'notes/note-add.html', {'form': form})


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
