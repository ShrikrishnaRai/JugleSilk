from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.views import View
from django.views.generic import ListView

from products.models import Product


class ProductsObjectMixin(object):
    model = Product

    def get_product(self):
        id = self.kwargs.get('id')
        productObject = None
        if id is not None:
            productObject = get_object_or_404(self.model, id=id)
        return productObject


class ListProducts(ListView):
    template_name = "products.html"
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            "object_list": self.get_queryset()
        }
        return render(request, self.template_name, context)


class GetProduct(ProductsObjectMixin, View):
    template_name = "productDetail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_product()}
        return render(request, self.template_name, context)
