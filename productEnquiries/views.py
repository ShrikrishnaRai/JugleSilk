from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.
from productEnquiries.models import productEnquiries


@csrf_protect
def createEnquiry(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        fullname = request.POST['fullname']
        enquiries = productEnquiries(email=email, address=address, fullName=fullname, phoneNumber=phone)
        enquiries.save()
        response = {
            "message": "Your enquiry saved successfully"
        }
        return render(request, 'productDetail.html', response)
