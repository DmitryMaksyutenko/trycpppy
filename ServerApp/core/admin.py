from django.contrib import admin

from blog.models import CategoriesLanguages


class CategoriesLanguagesInline(admin.TabularInline):
    """Class for many to many widgets."""
    model = CategoriesLanguages
    extra = 1


class CommonFields(admin.ModelAdmin):
    """Common options for Categories and Languages."""
    fields = ["name"]
    inlines = [CategoriesLanguagesInline]
