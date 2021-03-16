import os
from django.contrib.auth.models import User

from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import Group
from django.test.client import RequestFactory

from roles.models import Authors
from roles.admin import AuthorAdmin
from configs.settings.base import env

URL = "http://testserver/" + env("LOG_DIR")


class MockRequest:
    pass


class TestAuthorAdmin(TestCase):

    def setUp(self) -> None:
        self.site = AdminSite()
        self.ma = AuthorAdmin(Authors, self.site)

    def test_save_model(self):
        log_size_before = os.stat(env("LOG_DIR") + "/groups.log").st_size
        Group.objects.create(name="authors")
        user = User.objects.create_user(
            id=1,
            username="Name",
            password="0000",
            email="email@example.com"
        )
        request = RequestFactory().post(
            URL + "roles/authors/add/", {"user_id": 1})
        self.ma.save_model(
            request,
            Authors.objects.create(
                author_id=1,
                user_id=user
            ),
            {},
            False
        )
        log_size_after = os.stat(env("LOG_DIR") + "/groups.log").st_size
        self.assertNotEqual(log_size_before, log_size_after)

    def test_delete_model(self):
        log_size_before = os.stat(env("LOG_DIR") + "/groups.log").st_size
        grorup = Group.objects.create(name="authors")
        user = User.objects.create_user(
            id=1,
            username="Name",
            password="0000",
            email="email@example.com"
        )
        grorup.user_set.add(user)
        self.ma.delete_model(
            URL + "roles/authors/1/delete",
            user
        )
        log_size_after = os.stat(env("LOG_DIR") + "/groups.log").st_size
        self.assertNotEqual(log_size_before, log_size_after)

    def test_delete_queruset(self):
        log_size_before = os.stat(env("LOG_DIR") + "/groups.log").st_size
        grorup = Group.objects.create(name="authors")
        user1 = User.objects.create_user(
            id=1,
            username="Name",
            password="0000",
            email="email@example.com"
        )
        user2 = User.objects.create_user(
            id=2,
            username="New",
            password="0000",
            email="email@example.com"
        )
        grorup.user_set.add(user1)
        grorup.user_set.add(user2)
        self.ma.delete_queryset(
            URL + "roles/authors/1/delete",
            Authors.objects.all()
        )
        log_size_after = os.stat(env("LOG_DIR") + "/groups.log").st_size
        self.assertNotEqual(log_size_before, log_size_after)

    def test_change_view(self):
        grorup = Group.objects.create(name="authors")
        user = User.objects.create_superuser(
            id=1,
            username="Name",
            password="0000",
            email="email@example.com"
        )
        grorup.user_set.add(user)
        request = RequestFactory().get(URL + "roles/author/1/change/")
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        request.user = user
        self.ma.change_view(request, "1", form_url="", extra_context=None)
        self.assertEqual(self.ma.fields, ("description", "social"))
