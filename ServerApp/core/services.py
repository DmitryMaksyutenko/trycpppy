from django.db.models.query import QuerySet
from rest_framework.exceptions import NotFound


class BlogService:

    model = None

    def get_all(self) -> dict:
        pass

    def _get_all_or_NotFound(self) -> QuerySet:
        queryset = self.model.objects.all()
        if not any(queryset):
            raise NotFound
        return queryset

    def _combine_final_data(self, obj) -> dict:
        return {
            "count": len(obj.data),
            self.model_name: obj.data
        }

    def get_one(self) -> dict:
        pass

    def _uuid_from_request(self) -> str:
        return self.request.path.split("/")[-1]

    def _get_one_or_NotFound(self, uuid) -> object:
        try:
            return self.model.objects.get(uuid=uuid)
        except self.model.DoesNotExist:
            raise NotFound
