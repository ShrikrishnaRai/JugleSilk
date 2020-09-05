from django.urls import path
from .views import (
    ListCategories,
    GetProductByCategory
)

app_name = 'categories'
urlpatterns = [
    path('', ListCategories.as_view(), name='categories-list'),
    path('<int:pk>/', GetProductByCategory.as_view(), name='categories')
]
