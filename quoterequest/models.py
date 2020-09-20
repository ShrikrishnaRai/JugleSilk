from django.db import models

# Create your models here.
from products.models import Product
from datetime import datetime


class QuoteRequest(models.Model):
    fullName = models.CharField(max_length=120)
    address = models.CharField(max_length=120, null=True)
    email = models.EmailField()
    phoneNo = models.CharField(max_length=25, null=True)
    categories = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=datetime.now, editable=False, null=False, blank=False)
