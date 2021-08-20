
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from OnlineCookbook.recipes.models import Recipe


class IndexView(TemplateView):
    template_name = 'index.html'


# Search by keyword
class SearchRecipeView(ListView):
    model = Recipe
    template_name = 'recipes/list-recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        search_query = self.request.GET.get('search_field')
        object_list = Recipe.objects.filter(
                    Q(title__icontains=search_query) |
                    Q(ingredients__icontains=search_query) |
                    Q(type__contains=search_query)
                )
        return object_list
