import os

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite

from core.admin import UserAdmin
from configs.settings.base import env

URL = "http://testserver/" + env("ADMIN_URL")


class TestUserAdmin(TestCase):

    def setUp(self) -> None:
        User.objects.create(
            id=4,
            username="user",
            password="0000",
            email="some@mail.com"
        )
        self.users_log = env("LOG_DIR") + "/users.log"
        self.model = UserAdmin(model=User, admin_site=AdminSite())

    def test_new_user(self):
        "Test, new user creation."
        size_before = os.stat(self.users_log).st_size
        self.model.save_model(
            URL + "auth/add/",
            User.objects.create(
                id=10,
                username="Newuser",
                password="0000",
                email="some@mail.com"
            ),
            {},
            False
        )
        size_after = os.stat(self.users_log).st_size
        self.assertNotEqual(size_before, size_after)

    def test_user_change_name_to_same(self):
        """Test, log record not writes into the log file."""
        size_before = os.stat(self.users_log).st_size
        request = RequestFactory().post(URL + "auth/user/4/change/", {})
        user = User.objects.get(pk=4)
        self.model.save_model(request, user, form="", change=True)
        size_after = os.stat(self.users_log).st_size
        self.assertEqual(size_before, size_after)

    def test_user_change_name(self):
        """Test, log record writes into the log file."""
        size_before = os.stat(self.users_log).st_size
        request = RequestFactory().post(URL + "auth/user/4/change/", {})
        user = User.objects.get(pk=4)
        user.username = "New"
        self.model.save_model(request, user, form="", change=True)
        size_after = os.stat(self.users_log).st_size
        self.assertNotEqual(size_before, size_after)

    def test_user_deletion(self):
        "Test, user deletion."
        size_before = os.stat(self.users_log).st_size
        self.model.delete_model(
            URL + "auth/user/4/delete/",
            User.objects.get(pk=4)
         )
        size_after = os.stat(self.users_log).st_size
        self.assertNotEqual(size_before, size_after)

    def test_users_deletion(self):
        "Test, users deletion."
        User.objects.create(
            id=10,
            username="Newuser",
            password="0000",
            email="some@mail.com"
        )
        size_before = os.stat(self.users_log).st_size
        self.model.delete_queryset(
            URL + "auth/user/",
            User.objects.all()
         )
        size_after = os.stat(self.users_log).st_size
        self.assertNotEqual(size_before, size_after)

    def test_user_change_password(self):
        """Test, user password changing."""
        size_before = os.stat(self.users_log).st_size
        request = RequestFactory().post(
            URL + "auth/user/4/password/", {"password": "1234"})
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
        size_after = os.stat(self.users_log).st_size
        self.assertNotEqual(size_before, size_after)
