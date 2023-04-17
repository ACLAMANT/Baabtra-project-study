from django.shortcuts import render

from common.models import Customer

# Create your views here.

def c_home(request):
    return render(request, 'customer/homepage.html')

def c_mycart(request):
    return render(request, 'customer/mycart.html')

def c_myorders(request):
    return render(request, 'customer/myorders.html')

def c_changepassword(request):
    return render(request, 'customer/changepassword.html')
