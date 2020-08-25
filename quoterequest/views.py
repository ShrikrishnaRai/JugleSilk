from django.shortcuts import render
from .forms import QuoteReuqestForm


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
