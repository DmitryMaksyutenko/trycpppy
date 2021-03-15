from rest_framework import serializers

from api.mixins import RelatedMixin
from .categories import CategoriesSerializer
from blog.models import Categories, Languages


class LanguageSerializer(RelatedMixin, serializers.BaseSerializer):

    def __init__(self, instance, data, **kwargs):
        self.request = kwargs.pop("request")
        self.serializer = CategoriesSerializer
        self.queryset = Categories.objects.filter(
            languages=instance.language_id)
        super().__init__(instance=instance, data=data, **kwargs)

    def to_representation(self, instance):
        return {
            "name": instance.name,
            "categories": self.related_serialized_data()
        }


class LanguagesSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name="api:language",
        lookup_field="uuid"
    )

    class Meta:
        model = Languages
        fields = ("name", "link")
