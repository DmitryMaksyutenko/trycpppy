from django.test import TestCase
from rest_framework.exceptions import NotFound

from blog.models import Languages
from core.services import BlogService


class MockService(BlogService):

    def get_all(self) -> dict:
        pass

    def get_one(self) -> dict:
        pass


UUID = "eeee7bff-4ecc-46d3-9e4f-5c0f3698eeee"


class TestBlogService(TestCase):

    def test_model_DoesNotExists(self):
        """Testing the error raising."""
        service = MockService()
        service.model = Languages
        with self.assertRaises(NotFound):
            service._get_one_or_NotFound(UUID)

    def test_get_all(self):
        service = MockService()
        service.model = Languages
        self.assertEqual(service.get_all(), None)

    def test_get_one(self):
        service = MockService()
        service.model = Languages
        self.assertEqual(service.get_one(), None)
