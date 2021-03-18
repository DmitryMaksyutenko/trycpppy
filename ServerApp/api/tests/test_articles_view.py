from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from roles.models import Authors
from blog.models import (
    Articles, Languages, Categories, CategoriesLanguages
)
from core.tests.definitions import (
    BASE_TEST_URL, TEST_EMAIL, TEST_USERNAME, TEST_PASS,
    TEST_UUID_A, TEST_UUID_B, TEST_ARTICLE_CONTENT_A,
    TEST_ARTICLE_CONTENT_B
)

URL = BASE_TEST_URL + "api/articles/"


class TestArticlesView(APITestCase):
    """Tests for Articles API."""

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username=TEST_USERNAME,
            password=TEST_PASS,
            email=TEST_EMAIL
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
            name="data"
        )
        self.m2m = CategoriesLanguages.objects.create(
            id=1,
            language_id=self.language,
            category_id=self.category
        )
        self.article = Articles.objects.create(
            article_id=1,
            title="test title",
            content=TEST_ARTICLE_CONTENT_A,
            category=self.m2m,
            author=self.author,
            uuid=TEST_UUID_A
        )

    def test_get_article(self):
        """Testing, response return one article."""
        comparable_data = {
            "title": self.article.title,
            "content": self.article.content,
            "image": self.article.image,
            "code": self.article.code
        }
        url = reverse("api:article", kwargs={"uuid": self.article.uuid})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, comparable_data)

    def test_get_articles(self):
        """Testing, response return multiple articles."""
        a2 = Articles.objects.create(
            article_id=2,
            title="Test Title",
            category=self.m2m,
            author=self.author,
            uuid=TEST_UUID_B
        )
        comparable_data = {
            "count": 2,
            "articles": [
                {
                    "title": self.article.title,
                    "link": URL + TEST_UUID_A
                },
                {
                    "title": a2.title,
                    "link": URL + TEST_UUID_B
                },
            ]
        }
        url = reverse("api:articles")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, comparable_data)

    def test_no_articles(self):
        """Testing 404 not found."""
        self.article.delete()
        url = reverse("api:articles")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_article_search_success(self):
        """Testing, success search result."""
        a2 = Articles.objects.create(
            article_id=2,
            title="Test Title",
            content=TEST_ARTICLE_CONTENT_B,
            category=self.m2m,
            author=self.author,
            uuid=TEST_UUID_B
        )
        comparable_data = {
            "count": 2,
            "articles": [
                {
                    "title": self.article.title,
                    "link": URL + TEST_UUID_A
                },
                {
                    "title": a2.title,
                    "link": URL + TEST_UUID_B
                },
            ]
        }
        url = reverse("api:articles_search", kwargs={"value": "Ipsum."})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, comparable_data)

    def test_article_serarch_not_found(self):
        """Testing a failed search."""
        url = reverse("api:articles_search", kwargs={"value": "No data"})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
