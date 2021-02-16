from .base import * # noqa


# GENERAL
# =====================================================================
SECRET_KEY = env("SECRET_KEY") # noqa
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# CACHES
# =====================================================================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# =====================================================================
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
