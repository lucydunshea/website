import datetime

from django.utils import timezone
from django.db import models

# Create your models here.
class Project(models.Model):
    pub_date = models.DateTimeField("date published")
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)