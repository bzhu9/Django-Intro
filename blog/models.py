import uuid
from datetime import datetime
from django.db import models

# Create your models here.


class Post (models.Model):
    id = models.CharField(max_length=1000, blank=True, unique=True, primary_key=True, default=uuid.uuid4)
    author = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=500, default="")
    date = models.CharField(max_length=1000, blank=True, default=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def __str__(self):
        return self.id
