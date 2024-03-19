from django.urls import path
from .views import *
from .models import *
from django.conf.urls import include


urlpatterns = [
    path('list', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name = 'recipe_details'),
    path('accounts/', include('django.contrib.auth.urls')),
]

app_name = "ledger"