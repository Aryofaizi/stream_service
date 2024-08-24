from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Cart, CartItem
from content.models import Content, Genre

class CartTest(TestCase):
    """tests for the cart app."""
    
    @classmethod
    def setUpTestData(cls):
        cls.cart = Cart.objects.create()
        cls.cart.save()
        
        # use ContentTest instance to make a content
        cls.genre = Genre.objects.create(
            title = "Animated",
            description = """A film medium in which the film's images
            are primarily created by computer or hand and the characters are voiced by actors.""",
        )
        cls.genre.save()
        
        cls.content = Content.objects.create(
            title= "blind spot",
            description= "Blindspot is an American crime drama television series",
            release_date= "2015-09-21",
            category= "TVS",
            rate= "5",
            price= 12001,
        )
        cls.content.genre.add(cls.genre)
        cls.content.save()    
        
        
        cls.cart_item = CartItem.objects.create(cart=cls.cart, content=cls.content)
        cls.cart_item.save()
    
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
        
        
    def test_cart_item_create(self):
        """Tests if the creat cartitem endpoint returns 201 status code. """
        cart = Cart.objects.create()
        cart.save()
        url = reverse("cart-item-list", kwargs={"cart_pk":cart.id})
        payload = {
            "content": self.content.id
        }
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_cart_item_detail(self):
        """Tests cart item Detail, checks if the endpoint returns the
        specified cart item and status code:200"""
        url = reverse("cart-item-detail", kwargs={
            "cart_pk": self.cart.id,
            "pk": self.cart_item.id
            })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    