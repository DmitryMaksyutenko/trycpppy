from django.test import TestCase
from django.contrib.auth.models import User

from core.utils import user_to_string
from core.tests.definitions import (
    TEST_USERNAME, TEST_LASTNAME, TEST_PASS, TEST_EMAIL
)


class TestUtilsFunctions(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username=TEST_USERNAME,
            password=TEST_PASS,
            email=TEST_EMAIL
        )
        self.user.first_name = TEST_USERNAME
        self.user.last_name = TEST_LASTNAME
        self.user.save()

    def test_collect_string(self):
        """Testing the method for collect the string
           with the user informatio.
        """
        user_str = user_to_string(self.user)
        required_str = f"username={TEST_USERNAME}" + \
            f" first_name={TEST_USERNAME}" + \
            f" last_name={TEST_LASTNAME} email={TEST_EMAIL}"

        self.assertIsInstance(user_str, str)
        self.assertNotEqual(len(user_str), 0)
        self.assertEqual(user_str, required_str)
