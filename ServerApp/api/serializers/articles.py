from rest_framework import serializers

from blog.models import Articles


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ("title", "content", "image", "code")


class ArticlesSerializer(ArticleSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name="api:article",
        lookup_field="uuid"
    )

    class Meta(ArticleSerializer.Meta):
        fields = ("title", "link")
