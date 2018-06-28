from django.db import models

# Create your models here.

from django.utils import timezone
import datetime

class Product(models.Model):
    pub_date = models.DateTimeField('date uploaded')
    title = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    imgURL = models.ImageField(upload_to='Products/')
    def __str__(self):
        return self.title
