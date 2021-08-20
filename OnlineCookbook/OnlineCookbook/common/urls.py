from django.urls import path

from OnlineCookbook.common import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchRecipeView.as_view(), name='search recipes'),
]
