from rest_framework import serializers


class LanguageSerializer(serializers.BaseSerializer):

    def to_representation(self, instance):
        url = "/" + type(instance[0]).__name__.lower() + "/"
        languages_list = [
            {
                "id": str(language.uuid),
                "name": language.name,
                "link": url + str(language.uuid)
            }
            for language in instance
        ]
        data = {
            "count": len(instance),
            "languages": languages_list
        }
        return data
