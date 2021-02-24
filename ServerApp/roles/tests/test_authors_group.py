from django.test import TestCase
from django.contrib.auth.models import User

from roles.models import Authors


class TestAuthorGroup(TestCase):

    group_name = Authors.__name__.lower()

    def setUp(self) -> None:
        pass
