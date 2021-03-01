from django.test import TestCase
from django.contrib.auth.models import User, Group

from roles.models import Authors
from roles.services.custom_groups import AuthorGroup


class TestAuthorGroup(TestCase):

    group_name = Authors.__name__.lower()
    user_name = "Testuser"
    user_email = "test@mail.com"
    user_pass = "0000"

    def setUp(self) -> None:
        User.objects.create(
            id=1,
            username=self.user_name,
            email=self.user_email,
            password=self.user_pass
        )
        Group.objects.create(
            id=1,
            name=self.group_name
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
