from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LoginEndpointTests(APITestCase):
    def setUp(self):
        self.email = "user@test.dev"
        self.password = "test1234"
        get_user_model().objects.create_user(email=self.email, password=self.password)

    def test_login_returns_jwt_tokens(self):
        response = self.client.post(
            reverse("login"),
            {"email": self.email, "password": self.password},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_refresh_returns_new_access_token(self):
        login_response = self.client.post(
            reverse("login"),
            {"email": self.email, "password": self.password},
            format="json",
        )
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)

        refresh_response = self.client.post(
            reverse("token_refresh"),
            {"refresh": login_response.data["refresh"]},
            format="json",
        )

        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn("access", refresh_response.data)


class RegisterEndpointTests(APITestCase):
    def test_register_creates_user_and_returns_tokens(self):
        response = self.client.post(
            reverse("register"),
            {"email": "new@test.dev", "password": "test1234"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertTrue(get_user_model().objects.filter(email="new@test.dev").exists())

    def test_register_rejects_duplicate_email(self):
        get_user_model().objects.create_user(email="new@test.dev", password="test1234")

        response = self.client.post(
            reverse("register"),
            {"email": "new@test.dev", "password": "test1234"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
