from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Place(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    location = models.PointField()
