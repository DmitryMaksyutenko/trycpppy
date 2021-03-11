from rest_framework.exceptions import NotFound

from blog.models import Languages
from api.serializers.languages import LanguageSerializer


class LanguagesServeices:

    def __init__(self):
        self.model = Languages
        self.serializer = LanguageSerializer

    def get_all_languages(self, request):
        """Returns the all languages in database with meta data."""
        obj = self._get_all_or_NotFound()
        serialized = self.serializer(
            obj, many=True, context={"request": request})
        return self._add_languages_count(serialized)

    def _get_all_or_NotFound(self):
        obj = self.model.objects.all()
        if not any(obj):
            raise NotFound
        return obj

    def _add_languages_count(self, languages_list):
        """Adds the quantity of the serialized objects."""
        return {
            "count": len(languages_list.data),
            "languages": languages_list.data
        }
