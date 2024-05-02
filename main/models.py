"""a module for the object relation mapper to the database"""
from django.db import models


class User(models.Model):
    """
    User model for the member details
    """
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    address = models.TextField()
    password = models.TextField()
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    country = models.CharField(max_length=30)


class Server(models.Model):
    """Server information model"""
    id = models.IntegerField(null=False, primary_key=True)
    host = models.CharField(max_length=100)
    public_key = models.TextField()
    passphrase = models.CharField(max_length=50)
    ipaddress = models.GenericIPAddressField()