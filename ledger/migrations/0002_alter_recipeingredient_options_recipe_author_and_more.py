# Generated by Django 5.0.2 on 2024-03-18 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'verbose_name': 'Recipe Ingredient', 'verbose_name_plural': 'Recipe Ingredients'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='ledger.recipe'),
        ),
        migrations.AlterUniqueTogether(
            name='recipeingredient',
            unique_together={('ingredient', 'recipe')},
        ),
    ]
