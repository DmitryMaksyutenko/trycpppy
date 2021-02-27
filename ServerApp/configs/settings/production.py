from .base import * # noqa

DEBUG = env("DEBUG") # noqa

ADMINS = []

INSTALLED_APPS += [  # noqa
    "admin_honeypot"
]
