from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView)
from categories.models import Categories
from django.views import View


# Create your views here.


class CategoriesObjectMixin(object):
    model = Categories

    def get_category(self):
        id = self.kwargs.get('id')
        categoriesObject = None
        if id is not None:
            categoriesObject = get_object_or_404(self.model, id=id)
        return categoriesObject


class ListCategories(ListView):
    template_name = "categories.html"
    queryset = Categories.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            "object_list": self.get_queryset()
        }
        return render(request, self.template_name, context)


class GetCategory(CategoriesObjectMixin, View):
    template_name = "productDetail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_category()}
        return render(request, self.template_name, context)
