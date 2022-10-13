from django.db import models
from django.contrib.auth.models import User
import datetime

class tasklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length= 255)
    is_finished = models.BooleanField(default=False)
