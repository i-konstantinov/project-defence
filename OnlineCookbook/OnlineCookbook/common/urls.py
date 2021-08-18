from django.urls import path

from OnlineCookbook.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filtered/<str:dish_type>', views.recipe_type_filter, name='recipe type filter'),
    path('search/', views.search_recipes, name='search recipes'),
]
