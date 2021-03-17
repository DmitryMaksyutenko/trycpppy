from rest_framework.views import APIView
from rest_framework.response import Response

from blog.services.categories import CategoriesServices


class CategoriesView(APIView):
    """The view for the list of categories."""

    def get(self, request, *args, **kwargs):
        service = CategoriesServices(request)
        data = service.get_all()
        return Response(data)


class CategoryView(APIView):
    """The view for the category."""

    def get(self, request, *args, **kwargs):
        service = CategoriesServices(request)
        data = service.get_one()
        return Response(data)
