from datetime import datetime

from django.db import models


# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery", null=True)
    title = models.CharField(max_length=120, null=True)
    description = models.TextField(blank=True, null=True)
    uploadedBy = models.TextField(default="John Doe")
    created = models.DateTimeField(default=datetime.now, editable=False, null=False, blank=False)

