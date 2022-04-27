from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import Entry
from django.views.generic import (
    View,
    ListView
)


class EntryCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "entries/entry_create.html", {'form': EntryForm()})

    def post(self, request, *args, **kwargs):
        form = EntryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list-entries')

        return render(request, "entries/entry_create.html", {'form': form})


class EntryListView(ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = "entries/entry_list.html"
    ordering = ['-date_created', '-time_created']
    paginate_by = 3


class EntryUpdateView(View):
    def get(self, request, *args, **kwargs):
        element = Entry.objects.get(pk=kwargs['pk'])
        form = EntryForm(instance=element)
        context = {'form': form}
        return render(request, "entries/entry_create.html", context=context)

    def post(self, request, *args, **kwargs):
        element = Entry.objects.get(pk=kwargs['pk'])
        form = EntryForm(request.POST or None, instance=element)
        if form.is_valid():
            form.save()
            return redirect('list-entries')

        return render(request, "entries/entry_create.html", {'form': form})


def EntryDetailView(request, pk):
    entry = Entry.objects.get(pk=pk)
    return render(request, "entries/entry_detail.html", {'entry': entry})


def EntryDeleteView(request, pk):
    entry = Entry.objects.get(pk=pk)
    entry.delete()
    return redirect('list-entries')


def EntryDetailView(request, pk):
    context = {}
    entry = Entry.objects.get(pk=pk)
    context['entry'] = entry
    return render(request, "entries/entry_detail.html", context=context)
