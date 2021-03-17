from rest_framework import serializers

from blog.models import Articles


class ArticleSerializer(serializers.ModelSerializer):
    """Serializes the single model instance."""
    class Meta:
        model = Articles
        fields = ("title", "content", "image", "code")


class ArticlesSerializer(ArticleSerializer):
    """Serializes the multiple objects from the model with links."""

    link = serializers.HyperlinkedIdentityField(
        view_name="api:article",
        lookup_field="uuid"
    )

    class Meta(ArticleSerializer.Meta):
        fields = ("title", "link")
