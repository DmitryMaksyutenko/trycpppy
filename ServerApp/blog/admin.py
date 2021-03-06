import logging

from django.contrib import admin

from core.admin import CommonFields
from .models import (
    Languages, Categories, Articles
)

logger = logging.getLogger(__name__)


class LanguagesAdmin(CommonFields):
    """Custom settings."""


class CategoriesAdmin(CommonFields):
    """Custom settings"""
    list_filter = ("languages",)
    list_per_page = 10


class ArticlesAdmin(admin.ModelAdmin):
    """Custom settings"""
    list_display = ("title", "category")
    readonly_fields = ("uuid",)
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
        obj.image.name = obj.category.language_id.name + "/" + obj.image.name
        if change:
            logger.info(f"Updated article {obj.title}, from {obj.category}.")
        else:
            logger.info(f"Added new article {obj.title}, to {obj.category}.")
        super().save_model(request, obj, form, change)

    def delete_queryset(self, request, queryset) -> None:
        articles = [i.title.strip(".") for i in queryset]
        logger.info(f"Removed {', '.join(articles)}")
        return super().delete_queryset(request, queryset)

    def delete_model(self, request, obj) -> None:
        logger.info(f"{obj.title} removed from {obj.category}.")
        return super().delete_model(request, obj)


admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
