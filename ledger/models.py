from django.db import models
from django.urls import *

class Ingredient(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length = 100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete = models.CASCADE,
        related_name = 'recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete = models.CASCADE,
        related_name = 'ingredient'
    )

    def __str__(self):
        return f"{ self.recipe.name}: {self.quantity } of {self.ingredient}"

    def get_absolute_url():
        return reverse("recipeingredient_detail", args=[str(self.quantity)])