from django.test import TestCase
from django.urls import reverse


class CoreTest(TestCase):
    
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
        