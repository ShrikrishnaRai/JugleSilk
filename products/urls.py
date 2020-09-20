from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (ListProducts,
                    GetProduct,
                    product_list
                    )


app_name = 'products'
urlpatterns = [
    path('', ListProducts.as_view(), name='product-list'),
    path('<int:pk>/', GetProduct.as_view(), name='product'),
]
