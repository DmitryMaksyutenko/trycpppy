from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


from blog.models import (
    Articles, Languages, Categories, CategoriesLanguages
)
from roles.models import Authors

ARTICLE_DATA = "Data article"
ARTICLE_OOP = "OOP article"
CATEGORY_TYPES = "Data types."
CATEGORY_OOP = "OOP."
UUID_TYPES = "e88b7bff-4ecc-46d3-9e4f-5c0f3698ba19"
UUID_OOP = "aaab7bff-4ecc-46d3-9e4f-5c0f3698baaa"
UUID_ART_DATA = "dddd7bff-4ecc-46d3-9e4f-5c0f3698dddd"
UUID_ART_OOP = "cccb7bff-4ecc-46d3-9e4f-5c0f3698bccc"
URL_CAT = "http://testserver/api/categories/"
URL_ART = "http://testserver/api/articles/"


class TestCategoriesView(APITestCase):

    def test_get_all_catigories(self):
        Categories.objects.create(
            category_id=1,
            name=CATEGORY_TYPES,
            uuid=UUID_TYPES
        )
        Categories.objects.create(
            category_id=2,
            name=CATEGORY_OOP,
            uuid=UUID_OOP
        )
        categories = {
            "count": 2,
            "categories": [
                {
                    "name": CATEGORY_TYPES,
                    "link": URL_CAT + UUID_TYPES
                },
                {
                    "name": CATEGORY_OOP,
                    "link": URL_CAT + UUID_OOP
                },
            ]
        }
        url = reverse("api:categories")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, categories)

    def test_get_one_category(self):
        user = User.objects.create_user(
            "Name", "0000", "mail@example.com"
        )
        author = Authors.objects.create(
            author_id=1,
            user_id=user
        )
        language = Languages.objects.create(
            language_id=1,
            name="Python"
        )
        category = Categories.objects.create(
            category_id=1,
            name=CATEGORY_OOP
        )
        m2m = CategoriesLanguages.objects.create(
            id=1,
            language_id=language,
            category_id=category
        )
        Articles.objects.create(
            article_id=1,
            title=ARTICLE_DATA,
            category=m2m,
            author=author,
            uuid=UUID_ART_DATA
        )
        Articles.objects.create(
            article_id=2,
            title=ARTICLE_OOP,
            category=m2m,
            author=author,
            uuid=UUID_ART_OOP
        )
        categories = {
            "name": CATEGORY_OOP,
            "articles": [
                {
                    "title": ARTICLE_DATA,
                    "link": URL_ART + UUID_ART_DATA
                },
                {
                    "title": ARTICLE_OOP,
                    "link": URL_ART + UUID_ART_OOP
                },
            ]
        }
        url = reverse("api:category", kwargs={"uuid": category.uuid})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, categories)

    def test_no_languages(self):
        url = reverse("api:categories")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
