from rest_framework import serializers
from core.services import BlogService, SearchService
from blog.models import Articles
from api.serializers.articles import ArticlesSerializer, ArticleSerializer


class ArticlesServices(BlogService):

    model = Articles

    def __init__(self, request):
        self.request = request
        self.model_name = self.model.__name__.lower()

    def get_all(self):
        queryset = self._get_all_or_NotFound()
        serialized = ArticlesSerializer(
            queryset, many=True, context={"request": self.request})
        return self.resource_as_collection(serialized)

    def get_one(self):
        uuid = self._uuid_from_request()
        queryset = self._get_one_or_NotFound(uuid)
        serialized = ArticleSerializer(
            queryset, context={"request": self.request})
        return serialized.data


class SearchArticlesService(SearchService):

    model = Articles

    def __init__(self, request):
        self.request = request
        self.model_name = self.model.__name__.lower()

    def search(self, value):
        queryset = self._filter_or_NotFound(value)
        serialized = ArticlesSerializer(
            queryset, many=True, context={"request": self.request})
        return self.resource_as_collection(serialized)
