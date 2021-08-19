from django.urls import path

from OnlineCookbook.recipes import views


urlpatterns = [
    path('', views.ListRecipesView.as_view(), name='list recipes'),
    path('add/', views.AddRecipeView.as_view(), name='add recipe'),
    path('view/<int:pk>', views.RecipeDetailsView.as_view(), name='view recipe'),
    path('comment/<int:pk>', views.CommentRecipeView.as_view(), name='comment recipe'),
    path('like/<int:pk>', views.LikeRecipeView.as_view(), name='like recipe'),
    path('edit/<int:pk>', views.EditRecipeView.as_view(), name='edit recipe'),
    path('delete/<int:pk>', views.DeleteRecipeView.as_view(), name='delete recipe'),
]
