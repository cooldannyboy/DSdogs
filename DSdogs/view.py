#from django.http import
from django.shortcuts import render_to_response
from products.models import Product

def index(request):
    products = Product.objects.all

    return render_to_response('index.html', locals());
