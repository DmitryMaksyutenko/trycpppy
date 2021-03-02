import os

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite

from core.admin import UserAdmin
from configs.settings.base import env


class TestUserAdmin(TestCase):

    def setUp(self) -> None:
        User.objects.create(
            id=4,
            username="user",
            password="0000",
            email="some@mail.com"
        )
        self.users_log = env("LOG_DIR") + "/users.log"
        self.url_path = "/" + env("ADMIN_URL") + "auth/user/4/change/"
        self.model = UserAdmin(model=User, admin_site=AdminSite())

    def test_user_change_name_to_same(self):
        """Test, log record not writes into the log file."""
        size_before = os.stat(self.users_log).st_size
        request = RequestFactory().post(self.url_path, {})
        user = User.objects.get(pk=4)
        self.model.save_model(request, user, form="", change=True)
        size_after = os.stat(self.users_log).st_size

        self.assertEqual(size_before, size_after)

    def test_user_change_name(self):
        """Test, log record writes into the log file."""
        size_before = os.stat(self.users_log).st_size
        request = RequestFactory().post(self.url_path, {})
        user = User.objects.get(pk=4)
        user.username = "New"
        self.model.save_model(request, user, form="", change=True)
        size_after = os.stat(self.users_log).st_size

        self.assertNotEqual(size_before, size_after)
