
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from OnlineCookbook.common.forms import CommentForm
# from OnlineCookbook.common.models import Like
from OnlineCookbook.recipes.forms import RecipeForm
from OnlineCookbook.recipes.models import Recipe


def list_all_recipes(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/list-recipes.html', context)


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('list all recipes')
    else:
        form = RecipeForm()
        context = {
            'form': form,
        }
        return render(request, 'recipes/add-recipe.html', context)


# @login_required
# def comment_recipe(request, pk):
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.user = request.user
#         comment.save()
#     return redirect('view recipe', pk)


def view_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    recipe_owner = request.user == recipe.user

    # liked_by_current_user = recipe.like_set.filter(user_id=request.user.id).first()

    # total_number_of_likes = recipe.like_set.count()

    # comments = recipe.comment_set.all()

    recipe_ingredients = [f'- {i}\n' for i in recipe.ingredients.split()]

    context = {
        'recipe': recipe,
        'recipe_owner': recipe_owner,
        'recipe_ingredients': recipe_ingredients,
        # 'comments': comments,
        # 'comment_form': CommentForm(
        #     initial={'recipe_pk': pk}
        # ),
        # 'is_liked': liked_by_current_user is not None,
        # 'likes_count': total_number_of_likes,
    }
    return render(request, 'recipes/view-recipe.html', context)


@login_required
def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('view recipe', pk)
    else:
        form = RecipeForm(instance=recipe)
    context = {
        'recipe': recipe,
        'form': form,
    }
    return render(request, 'recipes/edit-recipe.html', context)


@login_required
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.delete()
    return redirect('index')


# @login_required
# def like_recipe(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     user = request.user
#
#     liked_by_current_user = recipe.like_set.filter(user_id=user.id).first()
#     if not liked_by_current_user:
#         like = Like(
#             recipe=recipe,
#             user=user,
#         )
#         like.save()
#     else:
#         liked_by_current_user.delete()
#     return redirect('view recipe', pk)
