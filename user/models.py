from django.db import models


# Create your models here.
class User(models.Model):
    username = models.TextField(max_length=255),
    password = models.TextField(max_length=50)
