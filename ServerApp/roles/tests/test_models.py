from django.test import TestCase
from django.contrib.auth.models import User

from roles.models import Authors


class TestAuthors(TestCase):

    def setUp(self) -> None:
        user = User.objects.create_user(
            "Name", "0000", "mail@example.com"
        )
        Authors.objects.create(
            author_id=1,
            user_id=user
        )

    def test_author_repr(self):
        author = Authors.objects.get(pk=1)
        self.assertEqual(str(author), "Name")
