from django.db import models


# Create your models here.
class QuoteRequest(models.Model):
    fullName = models.CharField(max_length=120)
    email = models.EmailField()
    categories = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
