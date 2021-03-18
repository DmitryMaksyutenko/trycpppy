import os
from pathlib import Path

import mock

from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.images import ImageFile

from blog.models import (
    Articles, Authors, Languages,
    Categories, CategoriesLanguages
)
from core.tests.definitions import (
    TEST_USERNAME, TEST_PASS, TEST_EMAIL,
    TEST_IMG_NAME
)


class TestArticles(TestCase):
    def setUp(self) -> None:
        self.img = mock.MagicMock(spec=ImageFile, name="img_mock")
        self.img.name = TEST_IMG_NAME
        self.IMG_PATH = settings.MEDIA_ROOT + self.img.name
        User.objects.create_user(
            id=1,
            username=TEST_USERNAME,
            password=TEST_PASS,
            email=TEST_EMAIL
        )
        self.author = Authors.objects.create(
            user_id=User.objects.get(pk=1),
            author_id=1
        )
        self.category = Categories.objects.create(
            category_id=1,
            name="test"
        )
        self.language = Languages.objects.create(
            language_id=1,
            name="Python"
        )
        self.cl = CategoriesLanguages.objects.create(
            id=1,
            language_id=Languages.objects.get(pk=1),
            category_id=Categories.objects.get(pk=1)
        )
        self.article = Articles.objects.create(
            article_id=1,
            title="test",
            author_id=1,
            image=self.img,
            category=CategoriesLanguages.objects.get(pk=1)
        )

    def tearDown(self) -> None:
        os.remove(self.IMG_PATH)

    def test_artileces_equal(self):
        """Testing the __eq__ method."""
        curr = Articles.objects.get(pk=1)
        new = Articles.objects.get(pk=1)
        self.assertEqual(curr, new)

    def test_articles_not_equal(self):
        """Testing the __ne__ method."""
        new = Articles(
            article_id=2,
            title="new test",
            author_id=1,
            image=self.img,
            category=self.cl
        )
        new.save()
        os.remove(new.image.path)
        self.assertNotEqual(self.article, new)

    def test_articles_user_update(self):
        """Testing, updating the existing article."""
        Articles.objects.filter(pk=1).update(title="new test")
        new = Articles.objects.get(pk=1)
        self.assertNotEqual(self.article, new)

    def test_no_content_and_content_vector(self):
        """Testing, if no content supplied,
            then content_vector is empty too.
        """
        self.assertFalse(self.article.content)
        self.assertFalse(self.article.content_vector)

    def test_delete_article_image(self):
        """Testing, the image must be removed from the media
           directory when an article is deleted.
        """
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

    def test_repr_str(self):
        """Testing the Articles representation string."""
        self.assertEqual(str(self.article), "test")


class TestCategories(TestCase):

    def test_repr_categories(self):
        """Testing the Categories representation string."""
        category = Categories.objects.create(
            category_id=1,
            name="Test category",
        )
        self.assertEqual(str(category), "Test category")


class TestLanguages(TestCase):

    def test_repr_lanuages(self):
        """Testing the Languages representation string."""
        language = Languages.objects.create(
            language_id=1,
            name="Python",
        )
        self.assertEqual(str(language), "Python")
