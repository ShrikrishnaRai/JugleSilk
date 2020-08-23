from django.db import models


# Create your models here.
class Blogs(models.Model):
    blogsImage = models.ImageField(upload_to='uploads/blogs/', null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
