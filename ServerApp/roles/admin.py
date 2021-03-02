import logging

from django.contrib import admin
from django.contrib.auth.models import User

from .models import Authors
from .services.custom_groups import AuthorGroup

logger = logging.getLogger(__name__)

<<<<<<< HEAD
=======

>>>>>>> e45fafcdcb1062c0ce3786d5af4b14ad11182f47

class AuthorAdmin(admin.ModelAdmin):
    """Custom settings."""
    fields = ("description", "social", "user_id")

    def save_model(self, request, obj, form, change) -> None:
        if not change:
            user = User.objects.get(pk=request.POST["user_id"])
            group = AuthorGroup()
            group.add(user)
            logger.info(f"{user.username} added to authors group.")
            super().save_model(request, obj, form, change)
        return

    def delete_model(self, request, obj) -> None:
        logger.info(f"{obj} removed from authors group.")
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset) -> None:
        names = [i.user_id.username for i in queryset]
        logger.info(f"{', '.join(names)} removed from authors group.")
        super().delete_model(request, queryset)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        self.fields = ("description", "social")
        return super().change_view(request, object_id, form_url, extra_context)

admin.site.register(Authors, AuthorAdmin)
