from django.urls import path

from OnlineCookbook.recipes import views


urlpatterns = [
    path('', views.list_all_recipes, name='list all recipes'),
    path('add/', views.add_recipe, name='add recipe'),
    path('view/<int:pk>', views.view_recipe, name='view recipe'),
    path('edit/<int:pk>', views.edit_recipe, name='edit recipe'),
    path('delete/<int:pk>', views.delete_recipe, name='delete recipe'),
    # path('comment/<int:pk>', views.comment_recipe, name='comment recipe'),
    # path('like/<int:pk>', views.like_recipe, name='like recipe'),

]