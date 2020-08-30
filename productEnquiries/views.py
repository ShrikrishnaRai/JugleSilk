from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


# Create your views here.


@csrf_protect
def createEnquiry(request):
    test = request.POST.get("exampleInputEmail1", "")
    context = {
        "test": test
    }
    return render(request, 'contactus.html', context)
