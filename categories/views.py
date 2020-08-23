from django.shortcuts import render, get_object_or_404

# Create your views here.
from categories.models import Categories


def product_categories(request, *args, **kwargs):
    queryset = Categories.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "category/categories.html", context)


def get_product_category(request, my_id):
    obj = get_object_or_404(Categories, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "category/detail.html", context)
