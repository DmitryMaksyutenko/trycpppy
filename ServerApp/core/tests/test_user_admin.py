import os

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite

from core.admin import UserAdmin
from configs.settings.base import env
from core.tests.definitions import (
    BASE_TEST_URL, TEST_USERNAME, TEST_PASS, TEST_EMAIL
)

ADMIN_URL = BASE_TEST_URL + env("ADMIN_URL")
LOG_URL = env("LOG_DIR") + "/users.log"


class TestUserAdmin(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            id=4,
            username=TEST_USERNAME,
            password=TEST_PASS,
            email=TEST_EMAIL
        )
        self.model = UserAdmin(model=User, admin_site=AdminSite())

    def test_new_user(self):
        "Testing, new user creation."
        size_before = os.stat(LOG_URL).st_size
        new_user = User.objects.create(
                id=10,
                username=TEST_USERNAME + "_new",
                password=TEST_PASS,
                email=TEST_EMAIL
        )
        self.model.save_model(ADMIN_URL + "auth/add/", new_user, {}, False)
        size_after = os.stat(LOG_URL).st_size
        self.assertNotEqual(size_before, size_after)

    def test_user_change_name_to_same(self):
        """Testing, log record not writes into the log file."""
        size_before = os.stat(LOG_URL).st_size
        request = RequestFactory().post(ADMIN_URL + "auth/user/4/change/", {})
        self.model.save_model(request, self.user, form="", change=True)
        size_after = os.stat(LOG_URL).st_size
        self.assertEqual(size_before, size_after)

    def test_user_change_name(self):
        """Testing, log record writes into the log file."""
        size_before = os.stat(LOG_URL).st_size
        request = RequestFactory().post(ADMIN_URL + "auth/user/4/change/", {})
        self.user.username = "New"
        self.model.save_model(request, self.user, form="", change=True)
        size_after = os.stat(LOG_URL).st_size
        self.assertNotEqual(size_before, size_after)

    def test_user_deletion(self):
        "Testing, user deletion."
        size_before = os.stat(LOG_URL).st_size
        self.model.delete_model(ADMIN_URL + "auth/user/4/delete/", self.user)
        size_after = os.stat(LOG_URL).st_size
        self.assertNotEqual(size_before, size_after)

    def test_users_deletion(self):
        "Testing, users deletion."
        User.objects.create(
            id=10,
            username=TEST_USERNAME + "_new",
            password=TEST_PASS,
            email=TEST_EMAIL
        )
        size_before = os.stat(LOG_URL).st_size
        self.model.delete_queryset(
            ADMIN_URL + "auth/user/",
            User.objects.all()
         )
        size_after = os.stat(LOG_URL).st_size
        self.assertNotEqual(size_before, size_after)

    def test_user_change_password(self):
        """Testing, user password changing."""
        size_before = os.stat(LOG_URL).st_size
        request = RequestFactory().post(
            ADMIN_URL + "auth/user/4/password/", {"password": "1234"})
        request.user = User.objects.create_superuser(
            id=1,
            username="Admin",
            password="0000",
            email="mail@example.com"
        )
        self.model.user_change_password(
            request,
            "1",
            form_url=""
        )
        size_after = os.stat(LOG_URL).st_size
        self.assertNotEqual(size_before, size_after)
