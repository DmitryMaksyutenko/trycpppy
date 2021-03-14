from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Languages, Categories, CategoriesLanguages


UUID_PY = "e88b7bff-4ecc-46d3-9e4f-5c0f3698ba19"
UUID_JS = "aaab7bff-4ecc-46d3-9e4f-5c0f3698baaa"
UUID_DATA = "abc34567-1111-46d3-9e4f-5c0f3698ba19"
UUID_OOP = "be435ad9-6666-46d3-9e4f-5c0f3698baaa"
PY = "Python"
JS = "JavaScript"
DATA = "Data category"
OOP = "OOP category"
URL_LANG = "http://testserver/api/languages/"
URL_CAT = "http://testserver/api/categories/"


class TestLanguageView(APITestCase):

    def test_get_many_languages(self):
        Languages.objects.create(
            language_id=1,
            name=PY,
            uuid=UUID_PY
        )
        Languages.objects.create(
            language_id=2,
            name=JS,
            uuid=UUID_JS
        )
        languages = {
            "count": 2,
            "languages": [
                {
                    "name": JS,
                    "link": URL_LANG + UUID_JS
                },
                {
                    "name": PY,
                    "link": URL_LANG + UUID_PY
                },
            ]
        }
        url = reverse("api:languages")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, languages)

    def test_get_one_language(self):
        language = Languages.objects.create(
            language_id=1,
            name=JS,
            uuid=UUID_JS
        )
        c1 = Categories.objects.create(
            category_id=1,
            name=DATA,
            uuid=UUID_DATA
        )
        c2 = Categories.objects.create(
            category_id=2,
            name=OOP,
            uuid=UUID_OOP
        )
        CategoriesLanguages.objects.create(
            id=1,
            language_id=language,
            category_id=c1
        )
        CategoriesLanguages.objects.create(
            id=2,
            language_id=language,
            category_id=c2
        )
        languages = {
            "name": JS,
            "categories": [
                {
                    "name": DATA,
                    "link": URL_CAT + UUID_DATA
                },
                {
                    "name": OOP,
                    "link": URL_CAT + UUID_OOP
                },
            ]
        }
        url = reverse("api:language", kwargs={"uuid": language.uuid})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, languages)

    def test_no_languages(self):
        url = reverse("api:languages")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
