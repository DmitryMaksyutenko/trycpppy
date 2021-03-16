from django.test import TestCase
from rest_framework.exceptions import NotFound

from blog.models import Languages
from core.services import BlogService


class TestBlogService(TestCase):

    def test_model_DoesNotExists(self):
        service = BlogService()
        service.model = Languages
        with self.assertRaises(NotFound):
            service._get_one_or_NotFound(
                "eeee7bff-4ecc-46d3-9e4f-5c0f3698eeee")

    def test_get_all(self):
        service = BlogService()
        service.model = Languages
        self.assertEqual(service.get_all(), None)

    def test_get_one(self):
        service = BlogService()
        service.model = Languages
        self.assertEqual(service.get_one(), None)
