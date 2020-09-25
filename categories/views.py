from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView)
from rest_framework import viewsets, permissions

from categories.models import Categories
from django.views import View

# Create your views here.
from categories.serializers import CategoriesSerializers
from products.models import Product


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
    permission_classes = [permissions.IsAuthenticated]


class ListCategories(ListView):
    template_name = "categories.html"
    queryset = Categories.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            "category_list": self.get_queryset()
        }
        return render(request, self.template_name, context)


class GetProductByCategory(ListView):
    model = Product
    template_name = 'products.html'

    def get(self, request, *args, **kwargs):
        categories = Categories.objects.get(id=self.kwargs['pk'])
        context = {
            "product_list": categories.products.all()
        }
        return render(request, self.template_name, context)
