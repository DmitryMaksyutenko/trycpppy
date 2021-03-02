from django.test import TestCase
from django.contrib.auth.models import User

from core.utils import user_to_string


class TestUtilsFunctions(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            "User", "mail@mail.com", "0000"
        )
        self.user.first_name = "Username"
        self.user.last_name = "Userlastname"
        self.user.save()

    def test_collect_string(self):
        user_str = user_to_string(self.user)
        required_str = f"username={self.user.username}" + \
            f" first_name={self.user.first_name}" + \
            f" last_name={self.user.last_name} email={self.user.email}"

        self.assertIsInstance(user_str, str)
        self.assertNotEqual(len(user_str), 0)
        self.assertEqual(user_str, required_str)
