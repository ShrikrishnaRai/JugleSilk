from django.urls import path
from .views import (ListProducts,
                    GetProduct
)

app_name = 'products'
urlpatterns = [
    path('', ListProducts.as_view(), name='product-list'),
    path('<int:id>/', GetProduct.as_view(), name='product')
]
