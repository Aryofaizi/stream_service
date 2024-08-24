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
        
    def test_cart_delete(self):
        """Tetst if the deletion process of the 
        specified cart."""
        url = reverse("cart-detail", kwargs={'pk': self.cart.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        

    def test_cart_item_list(self):
        """Tests the endpoint to retrieve the
        list of items for the specified cart."""
        url = reverse("cart-item-list", kwargs={"cart_pk": self.cart.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)