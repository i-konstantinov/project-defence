from django.conf.urls.static import static, settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OnlineCookbook.common.urls')),
    path('accounts/', include('OnlineCookbook.accounts.urls')),
    path('recipes/', include('OnlineCookbook.recipes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
