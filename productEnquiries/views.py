from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Create your views here.
from productEnquiries.models import productEnquiries
from products.models import Product


@csrf_protect
def createEnquiry(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        fullname = request.POST['fullname']
        product_id = request.POST['productId']
        product = Product.objects.get(id=product_id)
        enquiries = productEnquiries(product=product, email=email, address=address, fullName=fullname,
                                     phoneNumber=phone)
        enquiries.save()
        context = {
            "message": "Your enquiry saved successfully"
        }
        return redirect('/products/' + product_id, context)
