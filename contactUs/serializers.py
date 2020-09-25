from datetime import datetime

from django.db import models


# Create your models here.
from rest_framework import serializers

from contactUs.models import ContactUs


class ContactUsSerializers(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    message = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        return ContactUs.objects.create(**validated_data)