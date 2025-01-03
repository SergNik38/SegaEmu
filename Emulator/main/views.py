from django.shortcuts import render
from django.views.generic import ListView
from .models import Game


class GameListView(ListView):
    model = Game
    template_name = 'main/index.html'
    context_object_name = 'games'
    ordering = ['title']
