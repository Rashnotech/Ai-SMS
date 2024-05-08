"""a module for the object relation mapper to the database"""
from django.db import models
from django.conf import settings


class Server(models.Model):
    """Server information model"""
    id = models.IntegerField(null=False, primary_key=True)
    hostname = models.CharField(max_length=100, default='')
    public_key = models.TextField(default='')
    passphrase = models.CharField(max_length=50, default='')
    ipaddress = models.GenericIPAddressField(default='', unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default='', on_delete=models.CASCADE)
