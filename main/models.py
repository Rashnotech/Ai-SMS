"""a module for the object relation mapper to the database"""
from django.db import models


class Server(models.Model):
    """Server information model"""
    id = models.IntegerField(null=False, primary_key=True)
    host = models.CharField(max_length=100)
    public_key = models.TextField()
    passphrase = models.CharField(max_length=50)
    ipaddress = models.GenericIPAddressField()