from django import forms
from .models import Entry
import datetime
from taggit.forms import TagWidget


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'tags', 'date_created', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Enter Title'}),
            'tags': TagWidget(attrs={'class': 'form-control w-50', 'placeholder': 'Enter Tags Comma Seperated'}),
            'date_created': forms.DateInput(attrs={'type': 'date', 'class': 'form-control w-50', 'value': datetime.date.today().strftime("%Y-%m-%d"), 'max': datetime.date.today().strftime("%Y-%m-%d")}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'editorArea', 'placeholder': 'Enter Your Content here', 'id': 'entryArea'}),
        }
