from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status


class CoreTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.USER_USERNAME = "test2"
        cls.USER_PASSWORD = "usertest1234"
        cls.USER_EMAIL = "test2@gmail.com"
        cls.AUTH_TOKEN_PREFIX = "Token"
        
        cls.user = get_user_model().objects.create(
            username= cls.USER_USERNAME,
            email=cls.USER_EMAIL,
        )
        cls.user.set_password(cls.USER_PASSWORD) # Correctly hash the password
        cls.user.save() # Save the user with the hashed password
        
    def setUp(self):
        #register user to use the auth_Token
        register_url = reverse("login")
        register_payload = {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD,
        }
        response = self.client.post(path=register_url, data=register_payload, content_type="application/json")
        self.auth_token = response.json().get("auth_token")
    
    def test_register_user(self):
        """test for the register user endpoint
        i.e. make a new CustomUser"""
        url = reverse("customuser-list")
        payload = {
            "username": "test",
            "password": "usertest1234",
            "email": "test@gmail.com",
        }
        response = self.client.post(path=url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("username", response.json())
        self.assertIn("email", response.json())
        
        
    def test_login_user(self):
        """test for login user endpoint
        i.e. obtain a auth_token for existing user."""
        url = reverse("login")
        payload = {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD,
        }
        response = self.client.post(path=url,data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("auth_token", response.json())
        
        
        
    def test_logout_user(self):
        """test for logout user endpoint 
        i.e. token destroy."""
        url = reverse("logout")
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}",
        }
        response = self.client.post(path=url,content_type="application/json",
                                    headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        