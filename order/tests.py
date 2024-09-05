from django.test import TestCase
from django.urls import reverse
from config.tests import AuthMixin
from rest_framework import status
from .models import Order
from content.models import Content, Genre

class OrderTest(AuthMixin, TestCase):
    """A test class for order app."""
    
    def setUp(self):
        self.headers ={
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}",
        }
        
        self.order = Order.objects.create(user=self.user)
        # making content instance and genre
        self.genre = Genre.objects.create(
            title = "Animated",
            description = """A film medium in which the film's images
            are primarily created by computer or hand and the characters are voiced by actors.""",
        )
        self.genre.save()
        
        self.content = Content.objects.create(
            title= "blind spot",
            description= "Blindspot is an American crime drama television series",
            release_date= "2015-09-21",
            category= "TVS",
            rate= "5",
            price= 12001,
        )
        self.content.genre.add(self.genre)
        self.content.save()
    
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
        
        
    def test_order_detail(self):
        """test order detail endpoint"""
        url = reverse("order-detail", kwargs={'pk': self.order.id})
        response = self.client.get(path=url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        
    def test_order_item_list(self):
        """test order item list endpoint."""
        url = reverse("order-item-list",kwargs={"order_pk":self.order.id})
        response = self.client.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_item_create(self):
        """test order item list endpoint."""
        url = reverse("order-item-list",kwargs={"order_pk":self.order.id})
        """unit price in the payload is not important because it can be different based on the
         discounts or price from time to time on the website"""
        payload = {"content":self.content.id,"unit_price":12345}
        response = self.client.post(path=url, data=payload, content_type="application/json", headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
   