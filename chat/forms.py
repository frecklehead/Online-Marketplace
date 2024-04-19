from django import forms
from .models import chatmessages
class ChatmessagesForm(forms.ModelForm):
  class Meta:
    model=chatmessages
    fields=('content',)
    widgets={
      'content':forms.Textarea(attrs={
        'class':'w-full py-4 px-6 rounded-xl border'
      })
    }
