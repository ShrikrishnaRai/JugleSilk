from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
from categories.models import Categories


class Product(models.Model):
    productImage = models.ImageField(upload_to="product", null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(default='Best quality Pashmina')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name='products')
    colors = models.CharField(max_length=120, null=True)
