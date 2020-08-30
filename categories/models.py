from django.db import models
from django.urls import reverse


# Create your models here.
class Categories(models.Model):
    categoriesIconImage = models.ImageField(upload_to='uploads/categories/', null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(default='Best Quality Pashmina')

