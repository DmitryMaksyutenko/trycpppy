from django.contrib import admin

from .models import Authors


class AuthorAdmin(admin.ModelAdmin):
    """Custom settings."""
    fields = ("user_id",)


admin.site.register(Authors, AuthorAdmin)
