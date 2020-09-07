from django.http import HttpResponse
from django.shortcuts import render
from categories.models import Categories

# Create your views here.
from gallery.models import Gallery
from slider.models import Slider


def home_view(request, *args, **kwargs):
    galleries = Gallery.objects.all()
    slider_images = Slider.objects.all()
    context = {
        "galleries": galleries,
        "slider_images": slider_images
    }
    return render(request, "home.html", context)


def about_us(request, *args, **kwargs):
    return render(request, "about.html", {})
