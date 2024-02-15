from django.urls import path
from .views import get_recipe_list, get_recipe

urlpatterns = [
    path('recipes/list', get_recipe_list, name='List of Recipes'),
    path('recipe/1', get_recipe(1), name='Recipe 1'),
    path('recipe/2', get_recipe(2), name='Recipe 2')
]

app_name = "ledger"