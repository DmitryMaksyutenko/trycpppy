from rest_framework.fields import empty

from core.services import BlogService
from blog.models import Categories
from api.serializers.categories import CategoriesSerializer, CategorySerializer


class CategoriesServices(BlogService):

    model = Categories

    def __init__(self, request) -> None:
        self.request = request
        self.model_name = self.model.__name__.lower()

    def get_all(self):
        obj = self._get_all_or_NotFound()
        serialized = CategoriesSerializer(
            obj, many=True, context={"request": self.request})
        return self.resource_as_collection(serialized)

    def get_one(self):
        uuid = self._uuid_from_request()
        obj = self._get_one_or_NotFound(uuid)
        serialized = CategorySerializer(
            obj, data=empty, request=self.request)
        return serialized.data
