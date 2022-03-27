from dataclasses import field, fields
from django import forms
from .models import Entry
import datetime


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'date_created', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Enter Title'}),
            'date_created': forms.DateInput(attrs={'type': 'date', 'class': 'form-control w-50', 'value': datetime.date.today().strftime("%Y-%m-%d")}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'editorArea', 'placeholder': 'Enter Your Content here', 'id': 'entryArea'}),
        }
