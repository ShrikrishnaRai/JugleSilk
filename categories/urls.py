from django.urls import path
from .views import (
    ListCategories,
    GetCategory
)

app_name = 'categories'
urlpatterns = [
    path('', ListCategories.as_view(), name='categories-list'),
    path('<int:id>/', GetCategory.as_view(), name='category')
]
