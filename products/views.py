from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView

from categories.models import Categories
from products.models import Product


class ListProducts(ListView):
    template_name = "products.html"
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            "product_list": self.get_queryset()
        }
        return render(request, self.template_name, context)

    # This method is used to search product with product title from navbar
    def post(self, request, *args, **kwargs):
        queryset = Product.objects.filter(title=request.POST['title'])
        context = {
            "product_list": queryset
        }
        return render(request, self.template_name, context)


class GetProduct(DetailView):
    model = Product
    template_name = 'productDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(id=self.kwargs['pk'])
        context['product'] = product
        categories = Categories.objects.get(id=product.category.id)
        context['similar_products'] = categories.products.all()
        return context


