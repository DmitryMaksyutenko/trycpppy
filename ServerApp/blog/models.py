import operator

from django.db import models
from django.forms.models import model_to_dict
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

from core.models import CreatedUpdatedFields
from roles.models import Authors


class Languages(CreatedUpdatedFields):
    """The table for programming languages."""

    class Meta:
        ordering = ["name"]
        verbose_name = "Languages"
        verbose_name_plural = "Languages"
        indexes = [models.Index(fields=("uuid",))]

    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name


class Categories(CreatedUpdatedFields):
    """The table for categories of articles for the languages."""

    class Meta:
        ordering = ["name"]
        verbose_name = "Categories"
        verbose_name_plural = "Categories"
        indexes = [models.Index(fields=("uuid",))]

    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=56)
    languages = models.ManyToManyField(
        Languages,
        through="CategoriesLanguages"
    )

    def __str__(self) -> str:
        return self.name


class CategoriesLanguages(models.Model):
    """Many to Many intermidiate table."""

    id = models.AutoField(primary_key=True)
    language_id = models.ForeignKey(Languages, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.category_id.name + " " + self.language_id.name


class Articles(CreatedUpdatedFields):
    """The table for articles."""
    class Meta:
        verbose_name = "Articles"
        verbose_name_plural = "Articles"
        ordering = ["title"]
        indexes = [
            models.Index(fields=("category", "title")),
            GinIndex(fields=("content_vector",)),
            models.Index(fields=("uuid",))
        ]

    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=56)
    image = models.ImageField(max_length=132, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    content_vector = SearchVectorField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        CategoriesLanguages,
        on_delete=models.RESTRICT
    )
    author = models.ForeignKey(Authors, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.title

    def __eq__(self, obj) -> bool:
        """The Article objects are equale if their fields are equal."""
        curr = model_to_dict(self).values()
        new = model_to_dict(obj).values()
        if False in map(operator.eq, curr, new):
            return False
        return True

    def __ne__(self, obj) -> bool:
        return not self.__eq__(obj)

    def save(self, *args, **kwargs) -> None:
        self.content_vector = self.content
        super().save(*args, **kwargs)
