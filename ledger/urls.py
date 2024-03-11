from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('list', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name = 'recipe_details')
]

app_name = "ledger"