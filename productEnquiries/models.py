from django.db import models


# Create your models here.
class productEnquiries(models.Model):
    email = models.EmailField()
    fullName = models.TextField()
    phoneNumber = models.TextField()
    address = models.TextField()
