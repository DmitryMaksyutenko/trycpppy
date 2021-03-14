from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from blog.models import (
    Articles, Languages, Categories, CategoriesLanguages
)
from roles.models import Authors

UUID_A = "eeee7bff-4ecc-46d3-9e4f-5c0f3698eeee"
UUID_B = "aaaa7bff-4ecc-46d3-9e4f-5c0f3698aaaa"
URL = "http://testserver/api/articles/"


class TestArticlesView(APITestCase):

    def test_get_article(self):
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
            name="data"
        )
        m2m = CategoriesLanguages.objects.create(
            id=1,
            language_id=language,
            category_id=category
        )
        article = Articles.objects.create(
            article_id=1,
            title="test title",
            category=m2m,
            author=author
        )
        response_resource = {
            "title": article.title,
            "content": article.content,
            "image": article.image,
            "code": article.code
        }
        url = reverse("api:article", kwargs={"uuid": article.uuid})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_resource)

    def test_get_articles(self):
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
            name="data"
        )
        m2m = CategoriesLanguages.objects.create(
            id=1,
            language_id=language,
            category_id=category
        )
        a1 = Articles.objects.create(
            article_id=1,
            title="test title",
            category=m2m,
            author=author,
            uuid=UUID_A
        )
        a2 = Articles.objects.create(
            article_id=2,
            title="Test Title",
            category=m2m,
            author=author,
            uuid=UUID_B
        )
        response_resource = {
            "count": 2,
            "articles": [
                {
                    "title": a1.title,
                    "link": URL + UUID_A
                },
                {
                    "title": a2.title,
                    "link": URL + UUID_B
                },
            ]
        }
        url = reverse("api:articles")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_resource)

    def test_no_articles(self):
        url = reverse("api:articles")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
