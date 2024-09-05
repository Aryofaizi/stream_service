from django.test import TestCase
from django.urls import reverse
from config.tests import AuthMixin
from rest_framework import status

class OrderTest(AuthMixin, TestCase):
    """A test class for order app."""
    
    def setUp(self):
        self.headers ={
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}",
        }
    
    def test_order_list(self):
        """test order list endpoint."""
        url = reverse("order-list")
        response = self.client.get(path=url, content_type="application/json", headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_order_create(self):
        """test order create endpoint."""
        url = reverse("order-list")
        response = self.client.post(path=url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
