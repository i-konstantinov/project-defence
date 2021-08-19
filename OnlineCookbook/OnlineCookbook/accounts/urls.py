from django.urls import path

from OnlineCookbook.accounts import views


urlpatterns = [
    path('', views.ListProfilesView.as_view(), name='list profiles'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='log in'),
    path('logout/', views.UserLogoutView.as_view(), name='log out'),
    path('details/<int:pk>', views.ProfileDetailsView.as_view(), name='view profile'),
    path('edit/<int:pk>', views.ProfileEditView.as_view(), name='edit profile'),
]
