from django.db import models


class CreatedUpdatedFields(models.Model):
    """Abstract base model with common timestamp fields."""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        abstract = True
