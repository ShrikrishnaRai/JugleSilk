from django.http import HttpResponse
from django.shortcuts import render
from categories.models import Categories

# Create your views here.
from gallery.models import Gallery


def home_view(request, *args, **kwargs):
    galleries = Gallery.objects.all()
    context = {
        "galleries": galleries
    }
    return render(request, "home.html", context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_us(request, *args, **kwargs):
    return render(request, "about.html", {})
