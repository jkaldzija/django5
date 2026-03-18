from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class PingEndpointTests(APITestCase):
    def test_ping_returns_pong(self):
        response = self.client.get(reverse("ping"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "pong"})
