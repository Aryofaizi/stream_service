from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class CoreTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.USER_USERNAME = "test2"
        cls.USER_PASSWORD = "usertest1234"
        cls.USER_EMAIL = "test2@gmail.com"
        
        cls.user = get_user_model().objects.create(
            username= cls.USER_USERNAME,
            email=cls.USER_EMAIL,
        )
        cls.user.set_password(cls.USER_PASSWORD) # Correctly hash the password
        cls.user.save() # Save the user with the hashed password
        
    def setUp(self):
        # First, obtain a refresh token from login endpoint
        login_url = reverse("jwt-create")
        login_payload = {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD,
        }
        login_response = self.client.post(path=login_url, data=login_payload, content_type="application/json")
        self.refresh_token = login_response.json().get("refresh")
        self.access_token = login_response.json().get("access")
        
        
    
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
        self.assertEqual(response.status_code, 201)
        self.assertIn("username", response.json())
        self.assertIn("email", response.json())
        
        
    def test_login_user(self):
        """test for login user endpoint
        i.e. obtain a jwt for existing user."""
        url = reverse("jwt-create")
        payload = {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD,
        }
        response = self.client.post(path=url,data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("refresh", response.json())
        self.assertIn("access", response.json())
        
        
        
    def test_refresh_token(self):
        """test for refresh token endpoint 
        i.e. obtain an access token."""

        # Now, use the refresh token to obtain a new access token
        url = reverse("jwt-refresh")
        payload = {
            "refresh" : self.refresh_token
        }
        response = self.client.post(path=url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.json())
        
        