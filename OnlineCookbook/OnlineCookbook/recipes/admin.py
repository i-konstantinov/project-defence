from django.contrib import admin

from OnlineCookbook.recipes.models import Recipe


@admin.register(Recipe)
class OnlineCookbookRecipeAdmin(admin.ModelAdmin):
    pass
