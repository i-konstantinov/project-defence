from django.urls import path

from OnlineCookbook.accounts import views


urlpatterns = [
    path('', views.list_profiles, name='list profiles'),
    path('login/', views.log_in, name='log in'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='log out'),
    path('view/<int:pk>', views.view_profile, name='view profile'),
    path('edit/<int:pk>', views.edit_profile, name='edit profile'),
]