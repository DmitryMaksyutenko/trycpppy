from .base import * # noqa


DEBUG = True

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

# Logging
# =====================================================================
LOGGING["formatters"].update({ # noqa
    "console_log": {
        "format":
            "\n{levelname} {asctime}\nmodule = {module}\nmessage = {message}\n", # noqa
        "style": "{"
    },
})
LOGGING.update({ # noqa
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
})
LOGGING["handlers"].update({ # noqa
    "runserver": {
        "level": "DEBUG",
        "filters": ["require_debug_true"],
        "class": "logging.StreamHandler",
    },
    "debug": {
        "level": "DEBUG",
        "filters": ["require_debug_true"],
        "class": "logging.StreamHandler",
        "formatter": "console_log"
    },
})
LOGGING["loggers"].update({ # noqa
    "django": {
        "handlers": ["runserver"],
        "level": "INFO"
    },
})
LOGGING["loggers"]["roles.admin"]["handlers"].append("debug") # noqa
LOGGING["loggers"]["core.admin"]["handlers"].append("debug") # noqa
LOGGING["loggers"]["blog.admin"]["handlers"].append("debug") # noqa
LOGGING["loggers"]["roles.admin"]["level"] = "DEBUG" # noqa
LOGGING["loggers"]["core.admin"]["level"] = "DEBUG" # noqa
LOGGING["loggers"]["blog.admin"]["level"] = "DEBUG" # noqa
=======
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = "587"
EMAIL_HOST_USER = "1988maksyutenko@gmail.com"
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")  # noqa
ADMIN_HONEYPOT_EMAIL_ADMINS = True
