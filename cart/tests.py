from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class CartTest(TestCase):
    """tests for the cart app."""
        
    
    def test_cart_create(self):
        """Tests if the creat cart endpoint returns 201 status code."""
        url = reverse("cart-list")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    
        

