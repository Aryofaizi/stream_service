from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

class AuthMixin():
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.USER_USERNAME = "test2234567"
        cls.USER_PASSWORD = "usertest1234"
        cls.USER_EMAIL = "test2@gmail.com"
        cls.AUTH_TOKEN_PREFIX = "Token"
        
        cls.user = get_user_model().objects.create(
            username= cls.USER_USERNAME,
            email=cls.USER_EMAIL,
            is_staff=True,
        )
        cls.user.set_password(cls.USER_PASSWORD) # Correctly hash the password
        cls.user.save() # Save the user with the hashed password
        cls.login(cls)
        
    def login(self):
        #register user to use the auth_Token
        register_url = reverse("login")
        register_payload = {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD
        }
        response = self.client.post(path=register_url, data=register_payload, format="json")
        self.auth_token = response.json().get("auth_token")