from django.db import models
from datetime import datetime


# Create your models here.
class Blogs(models.Model):
    blogsImage = models.ImageField(upload_to='uploads/blogs/', null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.TextField(default="John Doe")
    created = models.DateTimeField(default=datetime.now, editable=False, null=False, blank=False)
