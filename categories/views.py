from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView)
from categories.models import Categories
from django.views import View

# Create your views here.
from products.models import Product


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
