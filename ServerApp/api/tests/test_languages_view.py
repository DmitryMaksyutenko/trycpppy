from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Languages, Categories, CategoriesLanguages
from core.tests.definitions import (
    BASE_TEST_URL, TEST_UUID_A, TEST_UUID_B, TEST_UUID_C,
    TEST_UUID_D, TEST_LANGUAGE_A, TEST_LANGUAGE_B, TEST_CATEGORY_A,
    TEST_CATEGORY_B
)

URL_LANG = BASE_TEST_URL + "api/languages/"
URL_CAT = BASE_TEST_URL + "api/categories/"


class TestLanguageView(APITestCase):
    """Tests for Languages API."""

    def setUp(self) -> None:
        self.language = Languages.objects.create(
            language_id=1,
            name=TEST_LANGUAGE_A,
            uuid=TEST_UUID_A
        )
        self.c1 = Categories.objects.create(
            category_id=1,
            name=TEST_CATEGORY_A,
            uuid=TEST_UUID_C
        )
        self.c2 = Categories.objects.create(
            category_id=2,
            name=TEST_CATEGORY_B,
            uuid=TEST_UUID_D
        )
        CategoriesLanguages.objects.create(
            id=1,
            language_id=self.language,
            category_id=self.c1
        )
        CategoriesLanguages.objects.create(
            id=2,
            language_id=self.language,
            category_id=self.c2
        )

    def test_get_one_language(self):
        """Testing, response return one language."""
        language = {
            "name": TEST_LANGUAGE_A,
            "categories": [
                {
                    "name": TEST_CATEGORY_A,
                    "link": URL_CAT + TEST_UUID_C
                },
                {
                    "name": TEST_CATEGORY_B,
                    "link": URL_CAT + TEST_UUID_D
                },
            ]
        }
        url = reverse("api:language", kwargs={"uuid": self.language.uuid})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, language)

    def test_get_many_languages(self):
        """Testing, response return multiple languages."""
        Languages.objects.create(
            language_id=2,
            name=TEST_LANGUAGE_B,
            uuid=TEST_UUID_B
        )
        languages = {
            "count": 2,
            "languages": [
                {
                    "name": TEST_LANGUAGE_B,
                    "link": URL_LANG + TEST_UUID_B
                },
                {
                    "name": TEST_LANGUAGE_A,
                    "link": URL_LANG + TEST_UUID_A
                },
            ]
        }
        url = reverse("api:languages")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, languages)

    def test_no_languages(self):
        """Testing 404 not found."""
        self.language.delete()
        url = reverse("api:languages")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
