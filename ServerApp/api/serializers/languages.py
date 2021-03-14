from rest_framework import serializers

from .categories import CategoriesSerializer
from blog.models import Categories, Languages


class LanguageSerializer(serializers.BaseSerializer):

    def __init__(self, instance, data, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(instance=instance, data=data, **kwargs)

    def to_representation(self, instance):
        obj = Categories.objects.filter(
            languages=instance.language_id)
        serialized = CategoriesSerializer(
            obj, many=True, context={"request": self.request}
        )
        return {
            "name": instance.name,
            "categories": serialized.data
        }


class LanguagesSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name="api:language",
        lookup_field="uuid"
    )

    class Meta:
        model = Languages
        fields = ("name", "link")
