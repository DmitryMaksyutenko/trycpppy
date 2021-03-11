from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Languages


UUID_PY = "e88b7bff-4ecc-46d3-9e4f-5c0f3698ba19"
UUID_JS = "aaab7bff-4ecc-46d3-9e4f-5c0f3698baaa"
PY = "Python"
JS = "JavaScript"
URL = "http://testserver/api/languages/"


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
                    "uuid": UUID_JS,
                    "name": JS,
                    "link": URL + UUID_JS
                },
                {
                    "uuid": UUID_PY,
                    "name": PY,
                    "link": URL + UUID_PY
                },
            ]
        }
        url = reverse("api:all_languages")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, languages)

    def test_get_one_language(self):
        Languages.objects.create(
            language_id=1,
            name=JS,
            uuid=UUID_JS
        )
        languages = {
            "count": 1,
            "languages": [
                {
                    "uuid": UUID_JS,
                    "name": JS,
                    "link": URL + UUID_JS
                },
            ]
        }
        url = reverse("api:all_languages")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, languages)

    def test_no_languages(self):
        url = reverse("api:all_languages")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
