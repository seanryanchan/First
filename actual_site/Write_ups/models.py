from django.db import models
from django.utils import timezone
import datetime

class Write_up(models.Model):
    id_name = models.CharField(max_length=64)
    title = models.CharField(max_length=256)
    content = models.TextField()
    pub_date = models.DateTimeField('date made')
    def __str__(self):
    	return self.id_name
