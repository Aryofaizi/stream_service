from django.db import models
from django.conf import settings
from django.urls import reverse


class Rate(models.TextChoices):
    PRODUCT_RATE_FIVE_STAR= 5, "EXCELLENT"
    PRODUCT_RATE_FOUR_STAR= 4, "GOOD"
    PRODUCT_RATE_THREE_STAR= 3, "NOT BAD"
    PRODUCT_RATE_TWO_STAR= 2, "BAD"
    PRODUCT_RATE_ONE_STAR= 1, "VERY BAD"
    
    
class Category(models.TextChoices):
    MOVIE = 'MOV', 'Movie'
    TV_SHOW = 'TVS', 'TV Show'
    MINI_SERIES = 'MIN', 'Mini-Series'
    ANTHOLOGY_SERIES = 'ANT', 'Anthology Series'
    WEB_SERIES = 'WEB', 'Web Series'
    DOCUMENTARY = 'DOC', 'Documentary'
    SPECIAL = 'SPE', 'Special'
    ANIMATED = 'ANI', 'Animated Film'
    REALITY = 'REA', 'Reality Show'
    TALK_SHOW = 'TAL', 'Talk Show'
    VARIETY_SHOW = 'VAR', 'Variety Show'

class Genre(models.Model):
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = [["title", "tmdb_id"]]
    
    def __str__(self):
        """Return genre title."""
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    category = models.CharField(
        max_length=3,
        choices=Category.choices,
        default=Category.MOVIE,
    )
    rate = models.CharField(choices=Rate.choices, max_length=16)
    price = models.PositiveIntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        """Return content title."""
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("content_detail", kwargs={"pk": self.pk})
    
    
    
class Comment(models.Model):
    STATUS_APPROVED ="a"
    STATUS_NOT_APPROVED = "na"
    STATUS_WAITING = "w"
    STATUS_CHOICES = [
        ("a", "approved"),
        ("na", "not-approved"),
        ('w', "waiting"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default=STATUS_WAITING)
    rate = models.CharField(choices=Rate.choices, max_length=16)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    

class Video(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="videos")
    file = models.FileField(upload_to="videos", max_length=255)
    
    def __str__(self) -> str:
        return self.content.title
    

class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="subtitles")
    language = models.CharField(max_length=10)  # Use language codes like "en", "fr"
    file = models.FileField(upload_to="subtitles")
    
    
    def __str__(self) -> str:
        return f"{self.video.content.title} subtitle"