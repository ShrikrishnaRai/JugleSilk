from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, DetailView
from rest_framework.parsers import JSONParser

from categories.models import Categories
from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        productList = Product.objects.all()
        serializer = ProductSerializer(productList, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


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
