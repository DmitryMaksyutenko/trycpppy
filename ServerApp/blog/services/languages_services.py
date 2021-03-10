from blog.models import Languages
from api.serializers.languages import LanguageSerializer


class LanguagesServeices:

    def __init__(self):
        self.model = Languages
        self.serializer = LanguageSerializer

    def get_all_languages(self):
        """Returns the all languages in database."""
        obj = self.model.objects.all()
        serializer = self.serializer(obj)
        return serializer.data
