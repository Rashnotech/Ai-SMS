from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    User model for the member details
    """
    email = models.EmailField(blank=True, default='', unique=True)
    telephone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['telephone', 'first_name', 'last_name']

    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]