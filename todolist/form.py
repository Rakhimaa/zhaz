from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Note


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользвателя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Pass', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title','discription','color']