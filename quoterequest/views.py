from django.shortcuts import render
from rest_framework import viewsets, permissions

from .forms import QuoteReuqestForm
from .models import QuoteRequest
from .serializers import SerializerForQuoteRequest


class QuoteRequestViewSet(viewsets.ModelViewSet):
    queryset = QuoteRequest.objects.all()
    serializer_class = SerializerForQuoteRequest
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.
def request_quote_view(request):
    form = QuoteReuqestForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = QuoteReuqestForm()
    context = {
        'form': form
    }
    return render(request, 'requestQuote.html', context)
