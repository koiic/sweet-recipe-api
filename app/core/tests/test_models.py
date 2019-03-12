from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_succeeds(self):
        """ Test successfully create user with email"""
        email = "test@calory.com"
        password = "calory20"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_user_email_succeeds(self):
        """ Test successfully normalize email"""

        email = "test@LONDON.COM"
        user = get_user_model().objects.create_user(
            email=email, password="test1234"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_with_invalid_email_fails(self):
        """ Test for Invalid email fails"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "pythondev")

    def test_create_new_super_user_succeeds(self):
        """test to create a super user"""
        email = "admin@calory.com"
        password = "calory20"
        user = get_user_model().objects.create_super_user(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
