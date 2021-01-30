from django import forms
from django.db import models


from .models import Note, Category


# добавляем временное поле, чтобы при выборе категории был не селектор, а простое поле для ввода
class CreateForm(forms.ModelForm):
    temp_category = forms.CharField(required=False)
    field_order = ['title_note','temp_category','content_note']
    class Meta:
        model = Note
        fields = '__all__'
        field_order = ['title_note','content_note']

        widgets = {
            'category_note': forms.HiddenInput()
        }
# функция, которая приводит параметры в нужную форму, тут же исправляем все ошибки    
    def clean(self):
        # если категория непустая 
        if  self.data['temp_category']:
            _mutable = self.data._mutable
            self.data._mutable = True
            self.data['temp_category'] = str(self.data['temp_category']).lower()
            try:
                chosen = Category.objects.get(name=self.data['temp_category'])
            except:
                new_cat = Category.objects.create(name=self.data['temp_category'])
                new_cat.save()
                self.cleaned_data['category_note'] = new_cat
            else:
                self.cleaned_data['category_note'] = chosen
            self.data._mutable = _mutable
        # если пользователь ничего не ввел
        else:
            if Category.objects.get(name='notag'):
                self.cleaned_data['category_note'] = Category.objects.get(name='notag')
            else:
                new_cat = Category.objects.create(name='notag')
                new_cat.save()
                self.cleaned_data['category_note'] = new_cat
        
           

    
    
   
    
