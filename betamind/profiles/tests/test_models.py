from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from profiles.models import UserProfile


class TestUserProfileModel(TestCase):

    def test_user_profile_model_created_successfully(self):
        """
        Test that a user profile model is created successfully, when
        an auth user model is created.
        """

        username = "testuser1"
        password = "testpassword1"

        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

        # Confirm that the post_save signal creates a user profile
        user_profile = get_object_or_404(UserProfile, pk=user.pk)

        self.assertEqual(user_profile.auth_user.username, username)
