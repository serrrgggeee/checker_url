from django.db import models
from django.contrib.auth.models import User


class Urls(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    url = models.URLField(max_length=200)
    active_time = models.TimeField(blank=True, null=True) 
