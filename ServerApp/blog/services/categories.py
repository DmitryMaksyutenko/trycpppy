from rest_framework.fields import empty
from rest_framework.exceptions import NotFound
from blog.models import Categories
from api.serializers.categories import CategoriesSerializer, CategorySerializer


class CategoriesServices:

    def __init__(self, request) -> None:
        self.model = Categories
        self.request = request

    def get_all(self):
        obj = self._get_all_or_NotFound()
        serialized = CategoriesSerializer(
            obj, many=True, context={"request": self.request})
        return self._add_count(serialized)

    def _get_all_or_NotFound(self):
        queryset = self.model.objects.all()
        if not any(queryset):
            raise NotFound
        return queryset

    def _add_count(self, obj):
        return {
            "count": len(obj.data),
            "categories": obj.data
        }

    def get_one(self):
        uuid = self.request.path.split("/")[-1]
        obj = self._get_one_or_NotFound(uuid)
        serialized = CategorySerializer(
            obj, data=empty, request=self.request)
        return serialized.data

    def _get_one_or_NotFound(self, uuid):
        try:
            return self.model.objects.get(uuid=uuid)
        except Categories.DoesNotExist:
            raise NotFound
        except Categories.MultipleObjectsReturned:
            raise NotFound
