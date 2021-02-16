from pathlib import Path
from os import path

import environ

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / "subdir".
# =====================================================================
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
APPS_DIR = path.dirname(BASE_DIR)

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

LOCALE_PATHS = (path.join(APPS_DIR, "locale"), )

# Databases.
# =====================================================================
DATABASES = {}

# URLs
# =====================================================================
ROOT_URLCONF = "configs.urls"
WSGI_APPLICATION = "configs.wsgi.application"


# Apps.
# =====================================================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Project applications.
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


# CSS, JavaScrip, Images e.t.c.
# =====================================================================
STATIC_URL = "/static/"


# Templates.
# =====================================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR) + "/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Logging.
# =====================================================================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
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
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
    }
}
