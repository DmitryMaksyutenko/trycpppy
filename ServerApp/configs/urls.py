from django.contrib import admin
from django.urls import path, include

from configs.settings.base import env


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path(env("ADMIN_URL"), admin.site.urls),
]
