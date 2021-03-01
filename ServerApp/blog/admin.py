from django.contrib import admin

from core.admin import CommonFields
from .models import (
    Languages, Categories, Articles
)


class LanguagesAdmin(CommonFields):
    """Custom settings."""


class CategoriesAdmin(CommonFields):
    """Custom settings"""
    list_filter = ("languages",)
    list_per_page = 10


class ArticlesAdmin(admin.ModelAdmin):
    """Custom settings"""
    list_display = ("title", "category")
    exclude = ("content_vector",)
    search_fields = ("title", "content_vector")
    list_per_page = 10
    list_filter = (
        "created",
        "category__language_id",
        "category__category_id"
    )

    def save_model(self, request, obj, form, change) -> None:
        obj.content_vector = request.POST["content"]
        super().save_model(request, obj, form, change)


admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
