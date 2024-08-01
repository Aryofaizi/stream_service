from django.db import models

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
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return genre title."""
        return self.title

class Content(models.Model):
    PRODUCT_RATE_FIVE_STAR = 5
    PRODUCT_RATE_FOUR_STAR = 4
    PRODUCT_RATE_THREE_STAR = 3
    PRODUCT_RATE_TWO_STAR = 2
    PRODUCT_RATE_ONE_STAR = 1
    PRODUCT_RATE_CHOICES = [
        (PRODUCT_RATE_FIVE_STAR, "EXCELLENT"),
        (PRODUCT_RATE_FOUR_STAR, "GOOD"),
        (PRODUCT_RATE_THREE_STAR, "NOT BAD"),
        (PRODUCT_RATE_TWO_STAR, "BAD"),
        (PRODUCT_RATE_ONE_STAR, "VERY BAD"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    category = models.CharField(
        max_length=3,
        choices=Category.choices,
        default=Category.MOVIE,
    )
    rate = models.IntegerField(choices=PRODUCT_RATE_CHOICES)
    price = models.PositiveIntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        """Return content title."""
        return self.title