from rest_framework.exceptions import NotFound
from rest_framework.fields import empty

from blog.models import Languages
from api.serializers.languages import LanguagesSerializer, LanguageSerializer


class LanguagesServeices:

    def __init__(self, request):
        self.model = Languages
        self.request = request

    def get_all(self):
        obj = self._get_all_or_NotFound()
        serialized = LanguagesSerializer(
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
            "languages": obj.data
        }

    def get_one(self):
        uuid = self.request.path.split("/")[-1]
        obj = self._get_one_or_NotFound(uuid)
        serialized = LanguageSerializer(
            obj, data=empty, request=self.request)
        return serialized.data

    def _get_one_or_NotFound(self, uuid):
        try:
            return self.model.objects.get(uuid=uuid)
        except Languages.DoesNotExist:
            raise NotFound
        except Languages.MultipleObjectsReturned:
            raise NotFound
