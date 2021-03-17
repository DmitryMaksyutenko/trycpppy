from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


from roles.models import Authors
from blog.models import (
    Articles, Languages, Categories, CategoriesLanguages
)
from core.tests.definitions import (
    BASE_TEST_URL, TEST_UUID_A, TEST_UUID_B, TEST_UUID_C,
    TEST_UUID_D, TEST_ARTICLE_A, TEST_ARTICLE_B, TEST_CATEGORY_A,
    TEST_CATEGORY_B
)

URL_CAT = BASE_TEST_URL + "api/categories/"
URL_ART = BASE_TEST_URL + "api/articles/"


class TestCategoriesView(APITestCase):
    """Tests for Categories API."""

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            "Name", "0000", "mail@example.com"
        )
        self.author = Authors.objects.create(
            author_id=1,
            user_id=self.user
        )
        self.language = Languages.objects.create(
            language_id=1,
            name="Python"
        )
        self.category = Categories.objects.create(
            category_id=1,
            name=TEST_CATEGORY_B,
            uuid=TEST_UUID_B
        )
        self.m2m = CategoriesLanguages.objects.create(
            id=1,
            language_id=self.language,
            category_id=self.category
        )
        Articles.objects.create(
            article_id=1,
            title=TEST_ARTICLE_A,
            category=self.m2m,
            author=self.author,
            uuid=TEST_UUID_C
        )
        Articles.objects.create(
            article_id=2,
            title=TEST_ARTICLE_B,
            category=self.m2m,
            author=self.author,
            uuid=TEST_UUID_D
        )

    def test_get_one_category(self):
        """Testing, response return one category."""
        category = {
            "name": TEST_CATEGORY_B,
            "articles": [
                {
                    "title": TEST_ARTICLE_A,
                    "link": URL_ART + TEST_UUID_C
                },
                {
                    "title": TEST_ARTICLE_B,
                    "link": URL_ART + TEST_UUID_D
                },
            ]
        }
        url = reverse("api:category", kwargs={"uuid": self.category.uuid})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, category)

    def test_get_all_catigories(self):
        """Testing, response return multiple categories."""
        Categories.objects.create(
            category_id=2,
            name=TEST_CATEGORY_A,
            uuid=TEST_UUID_A
        )
        categories = {
            "count": 2,
            "categories": [
                {
                    "name": TEST_CATEGORY_A,
                    "link": URL_CAT + TEST_UUID_A
                },
                {
                    "name": TEST_CATEGORY_B,
                    "link": URL_CAT + TEST_UUID_B
                },
            ]
        }
        url = reverse("api:categories")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, categories)

    def test_no_languages(self):
        """Testing 404 not found."""
        Articles.objects.all().delete()
        self.category.delete()
        url = reverse("api:categories")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
