from django.urls import path

from OnlineCookbook.common import views

urlpatterns = [
    path('', views.index, name='index')
]
