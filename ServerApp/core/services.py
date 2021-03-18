from abc import ABC, abstractmethod

from django.db.models.query import QuerySet
from rest_framework.exceptions import NotFound

from core.mixins import CollectionResourceMixine


class SearchService(CollectionResourceMixine, ABC):
    """The superclass contains common attributes
        and methods for searchin service.
    """

    model = None

    @abstractmethod
    def search(self, value):
        """Returns the dictionary with searched data."""

    def _filter_or_NotFound(self, value) -> QuerySet:
        """If there is no record, raise an axception."""
        queryset = self.model.objects.filter(
            content_vector=value
        )
        if not any(queryset):
            raise NotFound
        return queryset


class BlogService(CollectionResourceMixine, ABC):
    """The superclass contains common attributes
        and methods for the blog services.
    """

    model = None

    @abstractmethod
    def get_all(self) -> dict:
        """Returns the fienal dictionary with serilized data."""

    def _get_all_or_NotFound(self) -> QuerySet:
        """If there is no record, raise an axception."""
        queryset = self.model.objects.all()
        if not any(queryset):
            raise NotFound
        return queryset

    @abstractmethod
    def get_one(self) -> dict:
        """Returns the fienal dictionary with serilized data."""

    def _uuid_from_request(self) -> str:
        """Returns the uuid string retirieved from the request."""
        return self.request.path.split("/")[-1]

    def _get_one_or_NotFound(self, uuid) -> object:
        """If the correspondign record does not exist,
            then raise an exception.
        """
        try:
            return self.model.objects.get(uuid=uuid)
        except self.model.DoesNotExist:
            raise NotFound
