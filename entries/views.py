from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import Entry
from django.views.generic import (
    View,
    ListView
)
from django.contrib.auth.decorators import login_required


class EntryCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "entries/entry_create.html", {'form': EntryForm()})

    def post(self, request, *args, **kwargs):
        form = EntryForm(request.POST or None)
        if form.is_valid():
            form.instance.user_id = request.user.id
            form.save()
            return redirect('list-entries')

        return render(request, "entries/entry_create.html", {'form': form})


class EntryListView(ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = "entries/entry_list.html"
    paginate_by = 3

    def get_queryset(self):
        return Entry.objects.filter(
            user=self.request.user
        ).order_by('-date_created', '-time_created')


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


@login_required
def EntryDetailView(request, pk):
    entry = Entry.objects.get(pk=pk)
    if entry.user != request.user:
        return redirect('list-entries')
    return render(request, "entries/entry_detail.html", {'entry': entry})


@login_required
def EntryDeleteView(request, pk):
    entry = Entry.objects.get(pk=pk)
    entry.delete()
    return redirect('list-entries')
