from rest_framework.views import APIView
from rest_framework.response import Response

from blog.services.languages_services import LanguagesServeices


class RetrieveLanguages(APIView):
    def get(self, request, *args, **kwargs):
        service = LanguagesServeices()
        data = service.get_all_languages()
        return Response(data)
