from rest_framework.fields import empty

from core.services import BlogService
from blog.models import Languages
from api.serializers.languages import LanguagesSerializer, LanguageSerializer


class LanguagesServeices(BlogService):

    model = Languages

    def __init__(self, request):
        self.request = request
        self.model_name = self.model.__name__.lower()

    def get_all(self):
        obj = self._get_all_or_NotFound()
        serialized = LanguagesSerializer(
            obj, many=True, context={"request": self.request})
        return self.resource_as_collection(serialized)

    def get_one(self):
        uuid = self._uuid_from_request()
        obj = self._get_one_or_NotFound(uuid)
        serialized = LanguageSerializer(
            obj, data=empty, request=self.request)
        return serialized.data
