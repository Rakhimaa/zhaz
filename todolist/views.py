from contextlib import redirect_stderr
from msilib.schema import ListView
from multiprocessing import context
import re
from tkinter import W
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .form import UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import Note
from .form import NoteForm

from django.views.decorators.http import require_POST

def Todo(request):
    

    return render(request, 'todolist/index.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfuly registration')
            return redirect('login')
        else:
            messages.error(request, "You don't registration")
    else:
        form = UserCreationForm()
    return render(request, 'todolist/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = UserLoginForm()
    return render(request, 'todolist/login.html', {'form': form})


def main(request):
    return render(request, 'todolist/main.html')


def notion(request):

    form = NoteForm()

    note = Note.objects.all()
    return render(request, 'todolist/notion.html', {'notes': note, 'form': form})


@require_POST
def addNote(request):

    form = NoteForm(request.POST)

    if form.is_valid():
        new_note = Note(title=request.POST['title'], discription=request.POST['discription'], color=request.POST['color'])
        new_note.save()


    return redirect('notion')