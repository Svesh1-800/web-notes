from django import forms
from django.db import models


from .models import Note, Category


class CreateForm(forms.ModelForm):
    temp_category = forms.CharField()
    field_order = ['title_note','temp_category','content_note']
    class Meta:
        model = Note
        fields = '__all__'
        field_order = ['title_note','content_note']

        widgets = {
            'category_note': forms.HiddenInput()
        }
    
    def clean(self):
        try:
            chosen = Category.objects.get(name=self.data['temp_category'])
        except:
            new_cat = Category.objects.create(name=self.data['temp_category'])
            new_cat.save()
            self.cleaned_data['category_note'] = new_cat
        else:
            self.cleaned_data['category_note'] = chosen

        
           

    
    
   
    
