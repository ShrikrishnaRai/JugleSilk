from django.urls import path
from .views import (GetGallery, ListGallery
                    )

app_name = 'gallery'
urlpatterns = [
    path('', ListGallery.as_view(), name='Gallery-list'),
    path('<int:pk>/', GetGallery.as_view(), name='gallery')
]
