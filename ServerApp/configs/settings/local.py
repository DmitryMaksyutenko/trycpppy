from .base import * # noqa


DEBUG = True

ADMINS = [
    ("Dmitry", "up.dimamaksyutenko@gmail.com")
]

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
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = "587"
EMAIL_HOST_USER = "1988maksyutenko@gmail.com"
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")  # noqa
ADMIN_HONEYPOT_EMAIL_ADMINS = True
