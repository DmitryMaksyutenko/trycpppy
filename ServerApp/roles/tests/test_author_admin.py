import os

from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import Group
from django.test.client import RequestFactory

from roles.models import Authors
from roles.admin import AuthorAdmin
from configs.settings.base import env
from core.tests.definitions import (
    BASE_TEST_URL, TEST_USERNAME, TEST_EMAIL, TEST_PASS
)

URL = BASE_TEST_URL + env("LOG_DIR") + "roles/authors/"
GROUPS_LOG = env("LOG_DIR") + "/groups.log"
GROUP_NAME = "authors"
GROUP_LOG_PATH = env("LOG_DIR") + "/groups.log"


class MockRequest:
    pass


class TestAuthorAdmin(TestCase):
    """Tests for the AuthorAdmin class."""

    def setUp(self) -> None:
        self.site = AdminSite()
        self.ma = AuthorAdmin(Authors, self.site)
        self.user = User.objects.create_user(
            id=1,
            username=TEST_USERNAME,
            password=TEST_PASS,
            email=TEST_EMAIL
        )
        self.author = Authors.objects.create(
            author_id=1,
            user_id=self.user
        )
        self.group = Group.objects.create(name=GROUP_NAME)

    def test_save_model(self):
        """Testing, addition to the log record after
            the addition of the new author.
        """
        log_size_before = os.stat(GROUPS_LOG).st_size
        request = RequestFactory().post(URL + "add/", {"user_id": 1})
        self.ma.save_model(request, self.author, {}, False)
        log_size_after = os.stat(GROUPS_LOG).st_size
        self.assertNotEqual(log_size_before, log_size_after)

    def test_delete_model(self):
        """Testing, addition to the log record after
            deletion of the author.
        """
        log_size_before = os.stat(GROUP_LOG_PATH).st_size
        self.group.user_set.add(self.user)
        self.ma.delete_model(URL + "1/delete", self.user)
        log_size_after = os.stat(GROUP_LOG_PATH).st_size
        self.assertNotEqual(log_size_before, log_size_after)

    def test_delete_queruset(self):
        """Testing, addition to the log record after
            deletion of the QuerySet.
        """
        log_size_before = os.stat(GROUP_LOG_PATH).st_size
        user2 = User.objects.create_user(
            id=2,
            username=TEST_USERNAME + "_new",
            password=TEST_PASS,
            email=TEST_EMAIL
        )
        self.group.user_set.add(self.user)
        self.group.user_set.add(user2)
        queryset = Authors.objects.all()
        self.ma.delete_queryset(URL + "1/delete", queryset)
        log_size_after = os.stat(GROUP_LOG_PATH).st_size
        self.assertNotEqual(log_size_before, log_size_after)

    def test_change_view(self):
        """Testing, changing the visible fields on the view."""
        self.assertNotEqual(self.ma.fields, ("description", "social"))
        user = User.objects.create_superuser(
            id=1,
            username=TEST_USERNAME + "_new",
            password=TEST_PASS,
            email=TEST_EMAIL
        )
        self.group.user_set.add(user)
        request = RequestFactory().get(URL + "1/change/")
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        request.user = user
        self.ma.change_view(request, "1", form_url="", extra_context=None)
        self.assertEqual(self.ma.fields, ("description", "social"))
