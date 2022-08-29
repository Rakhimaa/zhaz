
from django.urls import path

from .views import Todo, notion, user_login, registration,main, notion, addNote

urlpatterns = [
    path('', Todo, name='home'),
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('main/', main, name='main'),
    path('notion/', notion, name='notion'),
    path('note', addNote, name='note')
]
