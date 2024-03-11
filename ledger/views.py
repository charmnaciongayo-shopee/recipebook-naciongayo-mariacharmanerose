from django.shortcuts import render
from .models import *

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'