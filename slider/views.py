from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from slider.models import Slider
from slider.serializers import SliderSerializers


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers
    permission_classes = [permissions.IsAuthenticated]
