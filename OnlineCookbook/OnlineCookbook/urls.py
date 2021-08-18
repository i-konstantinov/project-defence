
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OnlineCookbook.common.urls')),
    path('accounts/', include('OnlineCookbook.accounts.urls')),
    path('recipes/', include('OnlineCookbook.recipes.urls')),
]
