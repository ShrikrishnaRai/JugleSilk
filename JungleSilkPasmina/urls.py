"""JungleSilkPasmina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_us
from products.views import get_product, get_products
from categories.views import product_categories, get_product_category
from contactUs.views import contact_us_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('contactUs/', contact_us_view, name='contactUs'),
    path('about/', about_us, name='about'),
    path('admin/', admin.site.urls),
    path('product/<int:my_id>/', get_product, name='product'),
    path('category/<int:my_id>/', get_product_category, name='product_category'),
    path('categories/', product_categories, name='categories'),
    path('products/', get_products, name='products')
]
