
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from OnlineCookbook.common.models import Like, Comment
from OnlineCookbook.common.forms import CommentForm

from OnlineCookbook.recipes.forms import RecipeForm
from OnlineCookbook.recipes.models import Recipe


class ListRecipesView(ListView):
    model = Recipe
    template_name = 'recipes/list-recipes.html'
    context_object_name = 'recipes'


class AddRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/add-recipe.html'

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.user_id = self.request.user.id
        recipe.save()
        return redirect('recipe details')


class RecipeDetailsView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recipe = Recipe.objects.get(pk=self.kwargs.get('pk'))

        recipe_owner = self.request.user.id == recipe.user_id

        liked_by_current_user = recipe.like_set.filter(user_id=self.request.user.id).first()

        total_number_of_likes = recipe.like_set.count()

        comments = recipe.comment_set.all()

        context['recipe'] = recipe
        context['recipe_owner'] = recipe_owner
        context['liked_by_current_user'] = liked_by_current_user
        context['total_number_of_likes'] = total_number_of_likes
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context


"""Не използвам CreateView или FormView за Comment, защото изискват GET
и трябва да им се подаде темплейт"""


class CommentRecipeView(LoginRequiredMixin, View):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid() and not form.cleaned_data['text'] == '':
            recipe = Recipe.objects.get(pk=self.kwargs.get('pk'))
            comment = Comment(
                text=form.cleaned_data['text'],
                recipe=recipe,
                user=self.request.user,
            )
            comment.save()
            return redirect('recipe details', recipe.pk)

        else:
            return redirect('recipe details', self.kwargs.get('pk'))


class LikeRecipeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=self.kwargs.get('pk'))
        user = self.request.user

        liked_by_current_user = recipe.like_set.filter(user_id=self.request.user.id).first()

        if not liked_by_current_user:
            like = Like(
                recipe=recipe,
                user=user,
            )
            like.save()
        else:
            liked_by_current_user.delete()

        return redirect('recipe details', recipe.pk)


class EditRecipeView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/edit-recipe.html'

    def get_success_url(self):
        return reverse_lazy('recipe details', kwargs={'pk': self.kwargs['pk']})


"""Няма темплейт за показване на DeleteRecipeView при GET рикуест, затова пренаписвам метода"""


class DeleteRecipeView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('list recipes')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
