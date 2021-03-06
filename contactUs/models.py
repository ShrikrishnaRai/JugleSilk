from datetime import datetime

from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(null=True, max_length=255)
    email = models.EmailField(null=True, max_length=255)
    phone = models.CharField(null=True, max_length=255)
    message = models.TextField(null=True)
    address = models.CharField(null=True, max_length=255)
    created = models.DateTimeField(default=datetime.now, editable=False, null=False, blank=False)
