from django.contrib import admin
from django.contrib.auth.models import User

from .models import Authors
from .services.custom_groups import AuthorGroup


class AuthorAdmin(admin.ModelAdmin):
    """Custom settings."""
    list_display = ("user_id",)
    readonly_fields = ("user_id",)

    def save_model(self, request, obj, form, change) -> None:
        if not change:
            user = User.objects.get(pk=request.POST["user_id"])
            group = AuthorGroup()
            group.add(user)
            return super().save_model(request, obj, form, change)
        return


admin.site.register(Authors, AuthorAdmin)
