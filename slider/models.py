from datetime import datetime

from django.db import models


# Create your models here.
class Slider(models.Model):
    sliderImage = models.ImageField(upload_to="slider", null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    author = models.TextField(default="John Doe")
    created = models.DateTimeField(default=datetime.now, editable=False, null=False, blank=False)

