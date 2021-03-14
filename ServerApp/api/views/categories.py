from rest_framework.views import APIView
from rest_framework.response import Response

from blog.services.categories import CategoriesServices


class CategoriesView(APIView):

    def get(self, request, *args, **kwargs):
        service = CategoriesServices(request)
        data = service.get_all()
        return Response(data)


class CategoryView(APIView):

    def get(self, request, *args, **kwargs):
        service = CategoriesServices(request)
        data = service.get_one()
        return Response(data)
