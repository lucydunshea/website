import datetime

from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    pub_date = models.DateTimeField("date published")
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.title