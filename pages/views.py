from django.http import HttpResponse
from django.shortcuts import render
from categories.models import Categories


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_us(request, *args, **kwargs):
    return render(request, "about.html", {})

