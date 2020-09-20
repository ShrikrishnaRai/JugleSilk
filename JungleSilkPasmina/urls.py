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
from django.urls import path, include
from django.views.generic import TemplateView

from pages.views import home_view, about_us
from contactUs.views import contact_us_view
from quoterequest.views import request_quote_view
from productEnquiries.views import createEnquiry
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from pages.views import UserViewSet, GroupViewSet
from products.views import ProductViewSet

# urlpatterns += staticfiles_urlpatterns()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'product-list', ProductViewSet)

urlpatterns = [
    path('', home_view, name='home'),
    path('contactUs/', contact_us_view, name='contactUs'),
    path('blogs/', include('blogs.urls')),
    path('about/', about_us, name='about'),
    path('admin/', admin.site.urls),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('quoterequest/', request_quote_view, name='quoterequest'),
    path('productEnquiry/', createEnquiry, name='productEnquiry'),
    path('gallery/', include('gallery.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
