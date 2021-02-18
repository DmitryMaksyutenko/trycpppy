from django.contrib import admin

from .forms import ArticlesForm
from .models import (
    Languages, Categories, Articles
)


class LanguagesAdmin(admin.ModelAdmin):
    """Custom settings."""
    list_display = ("name",)


class CategoriesAdmin(admin.ModelAdmin):
    """Custom settings"""
    list_display = ("name", )
    list_filter = ("languages",)


class ArticlesAdmin(admin.ModelAdmin):
    """Custom settings"""
    form = ArticlesForm
    list_display = ("title",)
    search_fields = ("title", "content")
    list_filter = (
        "category_id__name",
        "category_id__languages",
        "created"
    )


admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
