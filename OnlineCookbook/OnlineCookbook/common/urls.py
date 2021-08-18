from django.urls import path

from OnlineCookbook.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filtered/<str:dish_type>', views.index_filter, name='index filter'),
    path('search/', views.search_recipes, name='search recipes'),
]
