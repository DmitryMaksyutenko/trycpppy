from django.contrib import admin

from .forms import ArticlesForm
from .models import (
    Languages, Categories, Articles, CategoriesLanguages
)


class CategoriesLanguagesInline(admin.TabularInline):
    model = CategoriesLanguages
    extra = 1


class LanguagesAdmin(admin.ModelAdmin):
    """Custom settings."""
    list_display = ("name",)
    inlines = (CategoriesLanguagesInline,)


class CategoriesAdmin(admin.ModelAdmin):
    """Custom settings"""
    list_display = ("name", )
    inlines = (CategoriesLanguagesInline,)
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
