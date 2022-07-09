from django.db import models
from datetime import datetime
from core.models import User
from .modelchoices import category_choices, platform_choices

# Create your models here.

class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=category_choices)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    platform = models.CharField(max_length=100, choices=platform_choices)
    total_rating = models.IntegerField(null=True)
    no_of_rating = models.IntegerField(null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    roadmap = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title
    