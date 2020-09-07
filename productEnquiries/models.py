from django.db import models

# Create your models here.
from products.models import Product


class productEnquiries(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='productenquiries')
    email = models.EmailField()
    fullName = models.TextField()
    phoneNumber = models.TextField()
    address = models.TextField()
