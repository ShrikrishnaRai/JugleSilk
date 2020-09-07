from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blogs.models import Blogs


class ListBlogs(ListView):
    template_name = "blogs.html"
    queryset = Blogs.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            "blogs": self.get_queryset()
        }
        return render(request, self.template_name, context)


class GetBlog(DetailView):
    model = Blogs
    template_name = 'blogsDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = Blogs.objects.get(id=self.kwargs['pk'])
        context['blog'] = blog
        return context
