from rest_framework import serializers

from .articles import ArticlesSerializer
from blog.models import Categories, Articles


class CategorySerializer(serializers.BaseSerializer):

    def __init__(self, instance, data, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(instance=instance, data=data, **kwargs)

    def to_representation(self, instance):
        obj = Articles.objects.filter(
            category__category_id=instance.category_id)
        serialized = ArticlesSerializer(
            obj, many=True, context={"request": self.request})

        return {
            "name": instance.name,
            "articles": serialized.data
        }


class CategoriesSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name="api:category",
        lookup_field="uuid"
    )

    class Meta:
        model = Categories
        fields = ("name", "link")
