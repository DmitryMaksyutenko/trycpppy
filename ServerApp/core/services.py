from abc import ABC, abstractmethod

from django.db.models.query import QuerySet
from rest_framework.exceptions import NotFound


class BlogService(ABC):
    """The superclass contains common actions for
        the blog services.
    """

    model = None

    @abstractmethod
    def get_all(self) -> dict:
        """Returns the fienal dictionary with serilized data."""

    def _get_all_or_NotFound(self) -> QuerySet:
        """Method for use in get_all()."""
        queryset = self.model.objects.all()
        if not any(queryset):
            raise NotFound
        return queryset

    def _combine_final_data(self, obj) -> dict:
        """Method for use in get_all()."""
        return {
            "count": len(obj.data),
            self.model_name: obj.data
        }

    @abstractmethod
    def get_one(self) -> dict:
        """Returns the fienal dictionary with serilized data."""

    def _uuid_from_request(self) -> str:
        """Method for use in get_one()."""
        return self.request.path.split("/")[-1]

    def _get_one_or_NotFound(self, uuid) -> object:
        """Method for use in get_one()."""
        try:
            return self.model.objects.get(uuid=uuid)
        except self.model.DoesNotExist:
            raise NotFound
