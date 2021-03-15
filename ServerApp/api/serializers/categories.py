from rest_framework import serializers

from .articles import ArticlesSerializer
from blog.models import Categories, Articles
from api.mixins import RelatedMixin


class CategorySerializer(RelatedMixin, serializers.BaseSerializer):

    def __init__(self, instance, data, **kwargs):
        self.request = kwargs.pop("request")
        self.serializer = ArticlesSerializer
        self.queryset = Articles.objects.filter(
            category__category_id=instance.category_id)
        super().__init__(instance=instance, data=data, **kwargs)

    def to_representation(self, instance):
        return {
            "name": instance.name,
            "articles": self.related_serialized_data()
        }


class CategoriesSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name="api:category",
        lookup_field="uuid"
    )

    class Meta:
        model = Categories
        fields = ("name", "link")
