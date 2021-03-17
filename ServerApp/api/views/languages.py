from rest_framework.views import APIView
from rest_framework.response import Response

from blog.services.languages import LanguagesServeices


class LanguagesView(APIView):
    """The view for the list of languages."""

    def get(self, request, *args, **kwargs):
        service = LanguagesServeices(request)
        data = service.get_all()
        return Response(data)


class LanguageView(APIView):
    """The view for the language."""

    def get(self, request, *args, **kwargs):
        service = LanguagesServeices(request)
        data = service.get_one()
        return Response(data)
