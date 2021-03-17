from django.test import TestCase
from django.contrib.auth.models import User, Group

from roles.services.custom_groups import AuthorGroup
from core.tests.definitions import (
    TEST_USERNAME, TEST_PASS, TEST_EMAIL
)

GROUP_NAME = "authors"


class TestAuthorGroup(TestCase):
    """Testing, a wrapper class for addition, and deletion
        of the user from the group.
    """

    def setUp(self) -> None:
        User.objects.create_user(
            id=1,
            username=TEST_USERNAME,
            password=TEST_PASS,
            email=TEST_EMAIL
        )
        Group.objects.create(
            id=1,
            name=GROUP_NAME,
        )

    def test_add_to_authors(self):
        """Add user to author group."""
        user = User.objects.get(pk=1)
        group = Group.objects.get(pk=1)
        author_group = AuthorGroup()
        author_group.add(user)
        self.assertTrue(user.groups.get(pk=group.id))

    def test_remove_from_authors(self):
        """Remove user from author group."""
        user = User.objects.get(pk=1)
        group = Group.objects.get(pk=1)
        author_group = AuthorGroup()
        author_group.add(user)
        author_group.remove(user)
        self.assertRaises(Group.DoesNotExist, user.groups.get, pk=group.id)
