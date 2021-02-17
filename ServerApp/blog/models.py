from django.db import models

from core.models import CreatedUpdatedFields


class Languages(CreatedUpdatedFields):
    """The table for programming languages."""
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
