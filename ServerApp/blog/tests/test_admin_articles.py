import os
from pathlib import Path
import mock

from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.images import ImageFile
from django.contrib.admin.sites import AdminSite

from configs.settings.base import env
from blog.admin import ArticlesAdmin
from blog.models import (
    Articles, Authors, Languages,
    Categories, CategoriesLanguages
)
from core.tests.definitions import (
    BASE_TEST_URL, TEST_IMG_NAME, TEST_USERNAME,
    TEST_PASS, TEST_EMAIL
)

URL = BASE_TEST_URL + env("ADMIN_URL") + "/articles/"
LOG_PATH = env("LOG_DIR") + "/articles.log"


class TestArticlesAdmin(TestCase):
    def setUp(self) -> None:
        self.site = AdminSite()
        self.ma = ArticlesAdmin(Articles, self.site)
        self.img = mock.MagicMock(spec=ImageFile, name="img_mock")
        self.img.name = TEST_IMG_NAME
        self.IMG_PATH = settings.MEDIA_ROOT + self.img.name
        User.objects.create_user(
            id=1,
            username=TEST_USERNAME,
            password=TEST_PASS,
            email=TEST_EMAIL
        )
        self.grup = Authors.objects.create(
            user_id=User.objects.get(pk=1),
            author_id=1
        )
        self.categry = Categories.objects.create(
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
            category=self.cl
        )

    def test_save_new_article(self):
        """Testing, when createing a new article, the new
           log racord about that action is adds to teh log file.
        """
        log_size_before = os.stat(LOG_PATH).st_size
        new_article = Articles.objects.create(
                article_id=2,
                title="Test",
                author_id=1,
                image=self.img,
                category=self.cl
            )
        self.ma.save_model(
            self.client.post(URL + "add/", {}),
            new_article,
            {},
            False
        )
        log_size_after = os.stat(LOG_PATH).st_size
        self.assertNotEqual(log_size_before, log_size_after)
        os.remove(self.article.image.path)
        os.remove(new_article.image.path)

    def test_change_article(self):
        """Testing, when change an article, the new
           log racord about that action is adds to teh log file.
        """
        log_size_before = os.stat(LOG_PATH).st_size
        self.article.title = "new"
        self.ma.save_model(
            self.client.post(URL + "1/change/", {}),
            self.article,
            {},
            True
        )
        log_size_after = os.stat(LOG_PATH).st_size
        self.assertNotEqual(log_size_before, log_size_after)
        os.remove(self.article.image.path)

    def test_article_deletion(self):
        """Testing, when delete an article, the image must be removed."""
        image = Path(self.article.image.path)
        os.remove(self.article.image.path)
        self.ma.delete_model(self.client.get(URL + "1/delete/"), self.article)
        self.assertFalse(image.exists())

    def test_deleteion_articles_set(self):
        """Testing, deleton an articles set."""
        articles = Articles.objects.all()
        os.remove(self.article.image.path)
        self.ma.delete_queryset(
            self.client.post(URL, {}),
            articles
        )
        self.assertEqual(len(Articles.objects.all()), 0)
