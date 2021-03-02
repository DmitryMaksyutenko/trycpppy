from .base import * # noqa

DEBUG = env("DEBUG") # noqa

SECRET_KEY = env("SECRET_KEY") # noqa

ADMINS = [
    ("", "")
]

INSTALLED_APPS += [  # noqa
]

# EMAIL
# =====================================================================
EMAIL_HOST = ""
EMAIL_USE_TLS = True
EMAIL_PORT = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")  # noqa
ADMIN_HONEYPOT_EMAIL_ADMINS = True

# Logging.
# =====================================================================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "handlers": {
        "django.server": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "INFO",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django": {
            "handlers": [""],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["mail_admins"],
            "level": "WARNING",
            "propagate": True,
        },
    }
}