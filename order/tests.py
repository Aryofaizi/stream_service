from django.test import TestCase
from django.urls import reverse
from config.tests import AuthMixin
from rest_framework import status

class OrderTest(AuthMixin, TestCase):
    """A test class for order app."""
    
    def test_order_list(self):
        """test order list endpoint."""
        url = reverse("order-list")
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}",
        }
        response = self.client.get(path=url, content_type="application/json", headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
