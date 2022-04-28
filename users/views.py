from tabnanny import check
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login

from users.forms import CustomUserForm


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list-entries')
        return render(request, "registration/register.html", {"form": CustomUserForm})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list-entries')
        form = CustomUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list-entries')

        return render(request, "registration/register.html", {"form": form})
