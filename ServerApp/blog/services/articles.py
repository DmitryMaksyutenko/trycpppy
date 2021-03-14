from rest_framework.exceptions import NotFound
from blog.models import Articles
from api.serializers.articles import ArticlesSerializer, ArticleSerializer


class ArticlesServices:

    def __init__(self, request):
        self.model = Articles
        self.request = request

    def get_all(self):
        queryset = self._get_all_or_NotFound()
        serialized = ArticlesSerializer(
            queryset, many=True, context={"request": self.request})
        return self._combine_final_data(serialized)

    def _get_all_or_NotFound(self):
        queryset = self.model.objects.all()
        if not any(queryset):
            raise NotFound
        return queryset

    def _combine_final_data(self, obj):
        return {
            "count": len(obj.data),
            "articles": obj.data
        }

    def get_one(self):
        uuid = self.request.path.split("/")[-1]
        queryset = self._get_one_or_NotFound(uuid)
        serialized = ArticleSerializer(
            queryset, context={"request": self.request})
        return serialized.data

    def _get_one_or_NotFound(self, uuid):
        try:
            return self.model.objects.get(uuid=uuid)
        except Articles.DoesNotExist:
            raise NotFound
        except Articles.MultipleObjectsReturned:
            raise NotFound
