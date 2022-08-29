from pyexpat import model
from ssl import create_default_context
from django.db import models
from django.conf import settings

COLOR_CHOICES = (
    ('green','GREEN'),
    ('pink', 'PINK'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


class Notion(models.Model):
    title = models.CharField(max_length=240)
    created = models.DateField(auto_now_add=True)
    body= models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    color= models.CharField(max_length=10)


class Note(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField(verbose_name='Body')
    color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='pink')

    def __str__(self):
        return self.title