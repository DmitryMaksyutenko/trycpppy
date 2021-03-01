from django.contrib import admin
from django.urls import path, include

from configs.settings.base import env


urlpatterns = [
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("grappelli/", include("grappelli.urls")),
    path(env("ADMIN_URL"), admin.site.urls),
]
