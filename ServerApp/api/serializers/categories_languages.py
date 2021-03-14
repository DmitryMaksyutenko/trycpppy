from rest_framework import serializers

from blog.models import CategoriesLanguages


class CategoriesLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesLanguages
        fields = ("category_id", "language_id")
