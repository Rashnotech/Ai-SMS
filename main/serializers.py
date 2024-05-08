#!/usr/bin/env python3
"""a module that handle class serialization"""
from rest_framework import serializers
from .models import Server


class ServerSerializer(serializers.ModelSerializer):
    """
    A class that inherits the serializer module to serialize class
    """
    class Meta:
        model = Server
        fields = ['hostname', 'public_key', 'passphrase', 'ipaddress']
