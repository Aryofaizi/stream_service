from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from config.tests import AuthMixin
from .models import Genre, Content

class ContentTest(AuthMixin,TestCase):
    """Tests for Content app."""
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        
        cls.genre = Genre.objects.create(
            title = "Animated",
            description = """A film medium in which the film's images
            are primarily created by computer or hand and the characters are voiced by actors.""",
        )
        cls.genre.save()
        
        
        url_create = reverse("content-list")
        payload_create = {
            "title": "blind spot",
            "description": "Blindspot is an American crime drama television series, created by Martin Gero, about a mysterious, heavily tattooed woman with no recollection of her past or identity.[1][2] It stars Sullivan Stapleton and Jaimie Alexander. Rob Brown, Audrey Esparza, Ashley Johnson, Ukweli Roach and Marianne Jean-Baptiste co-star.[3] Archie Panjabi, Luke Mitchell, Michelle Hurd, Ennis Esmer and Mary Elizabeth Mastrantonio joined the main cast in later seasons. The Warner Bros. Television-produced series premiered September 21, 2015, on NBC. On May 10, 2019, NBC renewed the series for a fifth and final season,[4] which aired from May 7[5] to July 23, 2020.",
            "release_date": "2015-09-21",
            "genre": [
                {
                    "title": "Animated"
                }
            ],
            "category": "TVS",
            "rate": "5",
            "price": 12001
        }
        headers_create = {
            "Authorization": f"{cls.AUTH_TOKEN_PREFIX} {cls.auth_token}",
        }
        cls.response = cls.client.post(path=url_create, data=payload_create, format="json", headers=headers_create)
        
        
    def test_content_create(self):
        """Tests the POST request to create a new content."""        
        
        url = reverse("content-list")
        payload = {
            "title": "Moana",
            "description": "Moana (also known as Vaiana[4] or Oceania[5] in some markets), is a 2016 American animated musical fantasy adventure film produced by Walt Disney Animation Studios and released by Walt Disney Pictures. The film was directed by John Musker and Ron Clements, co-directed by Chris Williams and Don Hall, and produced by Osnat Shurer, from a screenplay written by Jared Bush, and based on a story conceived by Clements, Musker, Williams, Hall, Pamela Ribon, and the writing team of Aaron Kandell and Jordan Kandell.",
            "release_date": "2016-11-14",
            "genre": [
                {
                    "title": "Animated"
                }
            ],
            "category": "ANI",
            "rate": "5",
            "price": 12000
        }
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}",
        }
        response = self.client.post(path=url, data=payload, content_type="application/json", headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.json())
        self.assertEqual(Content.objects.count(), 2) # it would return 2 because we have made one in the setUp
                
    
    def test_contents_list(self):
        """Test if retrieves a list of all content available."""
        url = reverse("content-list")
        response = self.client.get(path=url, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", response.json()[0]) # because it returns list and the dict is nested
        self.assertIn("title", response.json()[0])
    
    
    def test_contents_detail(self):
        """test if retrieves the details of a specific content by its ID. """
        url = reverse('content-detail', kwargs={'pk': 1})
        response = self.client.get(path=url, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", response.json())
        self.assertIn("title", response.json())
        
        

    def test_content_delete(self):
        """Tests the delete process of specified content."""
        url = reverse('content-detail', kwargs={'pk': 1})
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}",
        }
        response = self.client.delete(path=url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    