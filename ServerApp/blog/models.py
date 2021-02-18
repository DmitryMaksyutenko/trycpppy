from django.db import models
from django.contrib.postgres.search import SearchVectorField

from core.models import CreatedUpdatedFields
from roles.models import Author


class Languages(CreatedUpdatedFields):
    """The table for programming languages."""
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Categories(CreatedUpdatedFields):
    """The table for categories of articles for the languages."""
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=56)
    languages = models.ManyToManyField(Languages)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Articles(CreatedUpdatedFields):
    """The table for articles."""
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=56)
    image = models.CharField(max_length=32, null=True, blank=True)
    content = SearchVectorField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    category_id = models.ForeignKey(Categories, on_delete=models.RESTRICT)
    author_id = models.ForeignKey(Author, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
