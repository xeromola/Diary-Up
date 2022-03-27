from dataclasses import field, fields
from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'editorArea', 'placeholder': 'Enter Your Content here', 'id': 'entryArea'}),
        }
