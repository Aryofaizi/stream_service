from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from config.tests import AuthMixin
from .models import Genre, Content,Comment

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
        
        cls.comment = Comment.objects.create(
            user_id = cls.user.id,
            content = cls.content,
            text = "test comment",
            rate = 5,
            status = "a",
        )
        cls.comment.save()        
        
      
           
        
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
        self.assertIn("id", response.json().get("results")[0]) # because it returns list and the dict is nested
        self.assertIn("title", response.json().get("results")[0])
    
    
    def test_contents_detail(self):
        """test if retrieves the details of a specific content by its ID. """
        url = reverse('content-detail', kwargs={'pk': self.content.id})
        response = self.client.get(path=url, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", response.json())
        self.assertIn("title", response.json())
        
        

    def test_content_delete(self):
        """Tests the delete process of specified content."""
        url = reverse('content-detail', kwargs={'pk': self.content.id})
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}",
        }
        response = self.client.delete(path=url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Content.objects.count(), 0)
    
    def test_content_update(self):
        """Tests the update process of specified content."""
        url = reverse('content-detail', kwargs={'pk': self.content.id})
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}",
        }
        payload = {
            "title": "Moana edited title",
            "description": "edited description",
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
        response = self.client.patch(path=url, data=payload,
                                     content_type="application/json", headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        
    def test_comment_list(self):
        """Tests comment list, the endpoint must return
        the list of all approved comments."""
        url = reverse("content-comment-list", kwargs={"content_pk":1})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_comment_create(self):
        """Tests comment create, the endpoint must create
        a new comment."""
        url = reverse("content-comment-list", kwargs={"content_pk":self.content.id})
        payload = {
            "text":"test comment text!",
            "rate":5
        }
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}"
        }
        response = self.client.post(path=url, data=payload, headers=headers, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        

    def test_comment_detail(self):
        """Tests comment Detail, checks if the endpoint returns the
        specified comment and status code:200"""
        url = reverse("content-comment-detail",kwargs={"content_pk":self.content.id, "pk":self.comment.id})
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}"
        }
        response = self.client.get(path=url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("text", response.json())
        self.assertIn("rate", response.json())
        
        
    def test_comment_delete(self):
        """Tests if the comment speicified with the id would get deleted."""
        url = reverse("content-comment-detail",kwargs={"content_pk":self.content.id, "pk":self.comment.id})
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}"
        }
        response = self.client.delete(path=url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
        
    
    
    def test_comment_update(self):
        """Tests if the comment speicified with the id would get updated with new value."""
        url = reverse("content-comment-detail",kwargs={"content_pk":self.content.id, "pk":self.comment.id})
        headers = {
            "Authorization": f"{self.AUTH_TOKEN_PREFIX} {self.auth_token}"
        }
        payload = {
            "text": "this is the updated text for this comment",
            "rate": 5
        }
        response = self.client.patch(path=url, data=payload, headers=headers,
                                     content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(payload.get("text"), response.json().get("text"))  
        