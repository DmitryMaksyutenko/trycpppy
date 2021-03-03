import logging
import operator
import re

from django.contrib import admin
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from blog.models import CategoriesLanguages
from .utils import user_to_string

logger = logging.getLogger(__name__)


class CategoriesLanguagesInline(admin.TabularInline):
    """Class for many to many widgets."""
    model = CategoriesLanguages
    readonly_fields = ("category_id", "language_id")
    extra = 1


class CommonFields(admin.ModelAdmin):
    """Common options for Categories and Languages."""
    fields = ["name"]
    inlines = [CategoriesLanguagesInline]


class UserAdmin(BaseUserAdmin):

    def save_model(self, request, obj, form, change) -> None:
        if change:
            user = User.objects.get(pk=obj.id)
            if self._is_changed(user, obj):
                logger.info(
                    f"OLD'{user_to_string(user)}' NEW='{user_to_string(obj)}'")
            else:
                return
        else:
            logger.info(f"Created new user {obj}.")
        super().save_model(request, obj, form, change)

    def _is_changed(self, current, new) -> bool:
        """
        Compare, current with new.
        If they are the same, the user not modified.
        """
        cur_values = model_to_dict(current).values()
        new_values = model_to_dict(new).values()
        mapped = map(operator.eq, cur_values, new_values)
        if False in mapped:
            return True
        return False

    def delete_model(self, request, obj) -> None:
        logger.info(f"{obj} deleted.")
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset) -> None:
        names = [i.username for i in queryset]
        logger.info(f"{', '.join(names)} deleted.")
        super().delete_queryset(request, queryset)

    def user_change_password(self, request, id, form_url=""):
        username = User.objects.get(pk=id).username
        logger.info(f"User {username} password changed.")
        return super().user_change_password(request, id, form_url)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
