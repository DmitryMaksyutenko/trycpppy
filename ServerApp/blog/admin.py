from django.contrib import admin

from .models import (
    Languages, Categories
)


class LanguagesAdmin(admin.ModelAdmin):
    """Custom settings."""
    list_display = ("name",)


class CategoriesAdmin(admin.ModelAdmin):
    """Custom settings"""
    list_display = ("name", )


admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Categories, CategoriesAdmin)
