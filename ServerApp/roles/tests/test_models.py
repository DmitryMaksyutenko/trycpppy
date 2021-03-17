from django.test import TestCase
from django.contrib.auth.models import User

from roles.models import Authors
from core.tests.definitions import (
    TEST_USERNAME, TEST_PASS, TEST_EMAIL
)


class TestAuthors(TestCase):
    """Tests for the Authors model."""

    def setUp(self) -> None:
        user = User.objects.create_user(
            TEST_USERNAME,
            TEST_PASS,
            TEST_EMAIL
        )
        Authors.objects.create(
            author_id=1,
            user_id=user
        )

    def test_author_repr(self):
        """Testing the model printable representation."""
        author = Authors.objects.get(pk=1)
        self.assertEqual(str(author), TEST_USERNAME)
