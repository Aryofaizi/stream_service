from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Cart


class CartTest(TestCase):
    """tests for the cart app."""
    
    @classmethod
    def setUpTestData(cls):
        cls.cart = Cart.objects.create()
        cls.cart.save()
        
    
    def test_cart_create(self):
        """Tests if the creat cart endpoint returns 201 status code."""
        url = reverse("cart-list")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_cart_detail(self):
        """Tests if the cart specified with the uuid exists."""
        url = reverse("cart-detail", kwargs={'pk': self.cart.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        

