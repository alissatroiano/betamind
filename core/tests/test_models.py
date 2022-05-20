"""
Test for User Models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Test Models. """

    def test_create_user_without_email_successful(self):
        """ Test that creating a user without an email is successful. """

        username = "testuser123"
        password = "testpassword123"
        user = get_user_model().objects.create_user(
            username=username, password=password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
