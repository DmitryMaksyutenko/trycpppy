import uuid

from django.db import models


class CreatedUpdatedFields(models.Model):
    """Abstract base model with common timestamp fields."""

    class Meta:
        abstract = True

    uuid = models.UUIDField(default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
