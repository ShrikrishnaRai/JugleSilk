from django.shortcuts import render
from .forms import ContatctForm


# Create your views here.
def contact_us_view(request):
    form = ContatctForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContatctForm()
    context = {
        'form': form
    }
    return render(request, 'contactus.html', context)
