from .auth import User
from django.db import models
import datetime


class Shop(models.Model):
    title = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=500, null=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner_shops')
    revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date_created = models.DateTimeField(
        default=datetime.datetime.now)
    email = models.CharField(max_length=255,blank=True)
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    discordUrl = models.CharField(max_length=255,null=True,blank=True)
    discordId = models.IntegerField(null=True,blank=True)
    fbUrl = models.CharField(max_length=255,null=True,blank=True)
    instaUrl = models.CharField(max_length=255,null=True,blank=True)

