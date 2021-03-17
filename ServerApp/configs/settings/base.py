from pathlib import Path
from os import path

import environ

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / "subdir".
# =====================================================================
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# SECURITY WARNING: don"t run with debug turned on in production!
# =====================================================================
DEBUG = env("DEBUG")


# Internationalization.
# =====================================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (path.join(BASE_DIR, "locale"), )

# Databases.
# =====================================================================
DATABASES = {
    "default": env.db()
}

# URLs
# =====================================================================
ROOT_URLCONF = "configs.urls"
WSGI_APPLICATION = "configs.wsgi.application"


# Apps.
# =====================================================================
INSTALLED_APPS = [
    "grappelli",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",

    "admin_honeypot",
    "rest_framework",
    "PIL",

    # Project applications.
    "core",
    "roles",
    "blog",
    "api",
]


# Password validators.
# =====================================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", # noqa
    },
]


# Middleware.
# =====================================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


INTERNAL_IPS = ["127.0.0.1"]

# CSS, JavaScrip.
# =====================================================================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

#  Media files.
# =====================================================================
MEDIA_ROOT = env("MEDIA_ROOT")
MEDIA_URL = "media/"


# Templates.
# =====================================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR) + "/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]


# Logging
# =====================================================================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "file_log": {
            "format":
                "{levelname} {asctime} '{message}'",
            "style": "{"
        }
    },
    "handlers": {
        "file_users": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file_log",
            "filename": env("LOG_DIR") + "/users.log", # noqa
            "maxBytes": 1024
        },
        "file_groups": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file_log",
            "filename": env("LOG_DIR") + "/groups.log", # noqa
            "maxBytes": 1024
        },
        "file_articles": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file_log",
            "filename": env("LOG_DIR") + "/articles.log", # noqa
            "maxBytes": 1024
        }
    },
    "loggers": {
        "roles.admin": {
            "handlers": ["file_groups"],
            "level": "INFO",
        },
        "core.admin": {
            "handlers": ["file_users"],
            "level": "INFO",
        },
       "blog.admin": {
            "handlers": ["file_articles"],
            "level": "INFO",
        },
    }
}

# REST framework.
# =====================================================================
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": []
}
