from django.shortcuts import render

# Create your views here.
from blogs.models import Blogs


def blogs(request, *args, **kwargs):
    blog = Blogs.objects.all()
    context = {
        "blogs": blog
    }
    return render(request, "blogs.html", context)
