from django.contrib import admin

from .models import (
    Languages, Categories, Articles
)


class LanguagesAdmin(admin.ModelAdmin):
    """Custom settings."""
    list_display = ("name",)


class CategoriesAdmin(admin.ModelAdmin):
    """Custom settings"""
    list_display = ("name", )


class ArticlesAdmin(admin.ModelAdmin):
    """Custom settings"""
    list_display = ("title",)


admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
