from django.contrib import admin

from .models import (
    Languages
)


class LanguagesAdmin(admin.ModelAdmin):
    """Custom settings."""
    list_display = ("name",)


admin.site.register(Languages, LanguagesAdmin)
