from rest_framework import serializers
# from rest_framework.reverse import reverse

from blog.models import Languages


# class LanguageSerializer(serializers.BaseSerializer):

#     def __init__(self, instance, data, **kwargs):
#         self.request = kwargs.pop("request")
#         super().__init__(instance=instance, data=data, **kwargs)

#     def to_representation(self, instance):
#         return {
#             "uuid": str(instance.uuid),
#             "name": instance.name,
#             "link": reverse(
#                 "api:all_languages",
#                 args=[str(instance.uuid)],
#                 request=self.request
#             )
#         }


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(
        view_name='api:all_languages',
        lookup_field='uuid'
    )

    class Meta:
        model = Languages
        fields = ("uuid", "name", "link")
