
from django.shortcuts import render

from OnlineCookbook.common.forms import SearchForm
from OnlineCookbook.recipes.models import Recipe


def index(request):
    return render(request, 'index.html')


# Filter by type available only on index page
def recipe_type_filter(request, dish_type):
    recipes = Recipe.objects.filter(type=dish_type)

    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/list-recipes.html', context)


# Search by title
def search_recipes(request):
    form = SearchForm()
    recipes_found = []
    total_recipes_count = Recipe.objects.count()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data['text'].split(' ')

            for recipe in Recipe.objects.all():
                for keyword in keywords:
                    if recipe.title.lower().__contains__(keyword.lower()) \
                            or recipe.ingredients.lower().__contains__(keyword.lower()):
                        recipes_found.append(recipe)
    context = {
        'recipes': recipes_found,
        'form': form,
        'total_recipes_count': total_recipes_count,
    }
    return render(request, 'recipes/list-recipes.html', context)
