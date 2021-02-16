from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    """Custom settings."""
    list_display = ("user_id",)


admin.site.register(Author, AuthorAdmin)
