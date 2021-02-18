from django.contrib import admin

from core.admin import CategoriesLanguagesBaseAdmin
from .forms import ArticlesForm
from .models import (
    Languages, Categories, Articles
)


class LanguagesAdmin(CategoriesLanguagesBaseAdmin):
    """Custom settings."""


class CategoriesAdmin(CategoriesLanguagesBaseAdmin):
    """Custom settings"""
    list_filter = ("languages",)


class ArticlesAdmin(admin.ModelAdmin):
    """Custom settings"""
    form = ArticlesForm
    list_display = ("title",)
    search_fields = ("title", "content")
    list_filter = (
        "created",
        "category__language_id",
        "category__category_id"
    )


admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
