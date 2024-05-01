from django import forms
from .models import Item
CLASSES='w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
  class Meta:
    model=Item
    fields=('category','name','description','price','image',)
    widgets={
      'category':forms.Select(attrs={
        'class':CLASSES
      }),
      'name':forms.TextInput(attrs={
        'class':CLASSES
      }),
      'description':forms.Textarea(attrs={
        'class':CLASSES
      }),
      'price':forms.TextInput(attrs={
        'class':CLASSES
      }),
      'stock_quantity': forms.NumberInput(attrs={'class': CLASSES}),
      'image':forms.FileInput(attrs={
        'class':CLASSES
      })



    }
class EditItemForm(forms.ModelForm):
  class Meta:
    model=Item
    fields=('name','description','price','image','is_sold')
    widgets = {
      'name':forms.TextInput(attrs={
        'class':CLASSES
      }),
      'description':forms.Textarea(attrs={
        'class':CLASSES
      }),
      'price':forms.TextInput(attrs={
        'class':CLASSES
      }),
      'image':forms.FileInput(attrs={
        'class':CLASSES
      })
    }