import os
from pathlib import Path

import mock

from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.images import ImageFile

from blog.models import (
    Articles,
    Authors,
    Languages,
    Categories,
    CategoriesLanguages
)

IMG_NAME = "test.jpg"


class TestArticles(TestCase):
    def setUp(self) -> None:
        self.img = mock.MagicMock(spec=ImageFile, name="img_mock")
        self.img.name = IMG_NAME
        self.IMG_PATH = settings.MEDIA_ROOT + self.img.name
        User.objects.create_user(
            id=1,
            username="Testname",
            password="0000",
            email="test@mail.com"
        )
        Authors.objects.create(
            user_id=User.objects.get(pk=1),
            author_id=1
        )
        Categories.objects.create(
            category_id=1,
            name="test"
        )
        Languages.objects.create(
            language_id=1,
            name="Python"
        )
        CategoriesLanguages.objects.create(
            id=1,
            language_id=Languages.objects.get(pk=1),
            category_id=Categories.objects.get(pk=1)
        )
        Articles.objects.create(
            article_id=1,
            title="test",
            author_id=1,
            image=self.img,
            category=CategoriesLanguages.objects.get(pk=1)
        )

    def tearDown(self) -> None:
        os.remove(self.IMG_PATH)

    def test_artileces_equal(self):
        curr = Articles.objects.get(pk=1)
        new = Articles.objects.get(pk=1)
        self.assertEqual(curr, new)

    def test_articles_not_equal(self):
        curr = Articles.objects.get(pk=1)
        new = Articles(
            article_id=2,
            title="new test",
            author_id=1,
            image=self.img,
            category=CategoriesLanguages.objects.get(pk=1)
        )
        new.save()
        os.remove(new.image.path)
        self.assertNotEqual(curr, new)

    def test_articles_user_update(self):
        curr = Articles.objects.get(pk=1)
        Articles.objects.filter(pk=1).update(title="new test")
        new = Articles.objects.get(pk=1)
        self.assertNotEqual(curr, new)

    def test_no_content_and_content_vector(self):
        article = Articles.objects.get(pk=1)
        self.assertFalse(article.content)
        self.assertFalse(article.content_vector)

    def test_add_content(self):
        article = Articles.objects.get(pk=1)
        article.content = "Test content."
        article.save()
        self.assertTrue(article.content)
        self.assertTrue(article.content_vector)

    def test_delete_article_image(self):
        article = Articles.objects.create(
            article_id=2,
            title="test",
            author_id=1,
            image=self.img,
            category=CategoriesLanguages.objects.get(pk=1)
        )
        img_dir = Path(article.image.path)
        self.assertTrue(img_dir.exists())
        article.delete()
        self.assertFalse(img_dir.exists())
