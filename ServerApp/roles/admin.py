from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    """Custom settings."""
    fields = ("user_id",)


admin.site.register(Author, AuthorAdmin)
