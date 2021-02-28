from django.test import TestCase
from django.contrib.admin import ModelAdmin
from django.contrib.admin.sites import AdminSite

from roles.models import Authors


class MockRequest:
    pass


class TestAuthorAdmin(TestCase):

    def setUp(self) -> None:
        self.site = AdminSite()
        self.request = MockRequest()

    def test_default_fields(self):
        ma = ModelAdmin(Authors, self.site)
        self.assertEqual(ma.get_fields(self.request),
                         ["description", "social", "user_id"])
        self.assertEqual(list(ma.get_form(self.request).base_fields),
                         ["description", "social", "user_id"])
