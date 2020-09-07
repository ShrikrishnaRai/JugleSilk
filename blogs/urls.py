from django.urls import path
from .views import (ListBlogs,
                    GetBlog
                    )

app_name = 'blogs'
urlpatterns = [
    path('', ListBlogs.as_view(), name='blog-list'),
    path('<int:pk>/', GetBlog.as_view(), name='blog')
]
