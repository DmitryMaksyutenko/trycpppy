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
    Articles,
    Authors,
    Languages,
    Categories,
    CategoriesLanguages
)

IMG_NAME = "test.jpg"
URL = "http://testserver/" + env("ADMIN_URL") + "/articles/"


class TestArticlesAdmin(TestCase):
    def setUp(self) -> None:
        self.site = AdminSite()
        self.ma = ArticlesAdmin(Articles, self.site)
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

    def test_save_new_article(self):
        log_size_before = os.stat(env("LOG_DIR") + "/articles.log").st_size
        self.ma.save_model(
            self.client.post(URL + "add/", {}),
            Articles.objects.create(
                article_id=2,
                title="Test",
                author_id=1,
                image=self.img,
                category=CategoriesLanguages.objects.get(pk=1)
            ),
            {},
            False
        )
        log_size_after = os.stat(env("LOG_DIR") + "/articles.log").st_size
        self.assertNotEqual(log_size_before, log_size_after)
        os.remove(Articles.objects.get(pk=1).image.path)
        os.remove(Articles.objects.get(pk=2).image.path)

    def test_change_article(self):
        log_size_before = os.stat(env("LOG_DIR") + "/articles.log").st_size
        article = Articles.objects.get(pk=1)
        article.title = "new"
        self.ma.save_model(
            self.client.post(URL + "1/change/", {}),
            article,
            {},
            True
        )
        log_size_after = os.stat(env("LOG_DIR") + "/articles.log").st_size
        self.assertNotEqual(log_size_before, log_size_after)
        os.remove(Articles.objects.get(pk=1).image.path)

    def test_article_deletion(self):
        image = Path(Articles.objects.get(pk=1).image.path)
        article = Articles.objects.get(pk=1)
        os.remove(Articles.objects.get(pk=1).image.path)
        self.ma.delete_model(
            self.client.get(URL + "1/delete/"),
            article
        )
        self.assertFalse(image.exists())

    def test_deleteion_articles_set(self):
        articles = Articles.objects.all()
        os.remove(Articles.objects.get(pk=1).image.path)
        self.ma.delete_queryset(
            self.client.post(URL, {}),
            articles
        )
        self.assertEqual(len(Articles.objects.all()), 0)
