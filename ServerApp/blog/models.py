from django.db import models

from core.models import CreatedUpdatedFields


class Languages(CreatedUpdatedFields):
    """The table for programming languages."""
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name


class Categories(CreatedUpdatedFields):
    """The table for categories of articles for the languages."""
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=56)
    languages = models.ManyToManyField(Languages)

    def __str__(self) -> str:
        return self.name
