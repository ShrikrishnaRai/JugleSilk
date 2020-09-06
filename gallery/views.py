from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from gallery.models import Gallery


class ListGallery(ListView):
    template_name = "gallery.html"

    def get(self, request, *args, **kwargs):
        context = {
            "galleries": Gallery.objects.all()
        }
        return render(request, self.template_name, context)


class GetGallery(DetailView):
    model = Gallery
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery = Gallery.objects.get(id=self.kwargs['pk'])
        context['gallery'] = gallery
        return context
