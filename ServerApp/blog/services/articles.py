from core.services import BlogService
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
        return self._combine_final_data(serialized)

    def get_one(self):
        uuid = self._uuid_from_request()
        queryset = self._get_one_or_NotFound(uuid)
        serialized = ArticleSerializer(
            queryset, context={"request": self.request})
        return serialized.data
