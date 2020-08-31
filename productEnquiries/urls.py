from django.urls import path
from .views import (createEnquiry)

app_name = 'productEnquiries'
urlpatterns = [
    path('', createEnquiry, name='productEnquiries')
]
