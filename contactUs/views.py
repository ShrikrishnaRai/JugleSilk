from django.shortcuts import render
from rest_framework import viewsets, permissions

from .forms import ContactForm
from .models import ContactUs
from .serializers import ContactUsSerializers


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.
def contact_us_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contactus.html', context)
