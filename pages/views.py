from django.http import HttpResponse
from django.shortcuts import render
from categories.models import Categories

# Create your views here.
from gallery.models import Gallery
from slider.models import Slider
from products.views import product_list

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pages.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


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
