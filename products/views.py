from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from products.models import Product


def get_product(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "product/detail.html", context)


def get_products(request, *args, **kwargs):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "product/products.html", context)
