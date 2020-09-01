from django.db import models


# Create your models here.
class QuoteRequest(models.Model):
    fullName = models.CharField(max_length=120)
    address = models.CharField(max_length=120, null=True)
    email = models.EmailField()
    phoneNo = models.CharField(max_length=25)
    categories = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
