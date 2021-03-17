from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

from configs.settings.base import env


urlpatterns = [
    path("api/", include("api.urls", namespace="api")),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("grappelli/", include("grappelli.urls")),
    path(env("ADMIN_URL"), admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
