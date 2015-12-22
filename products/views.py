from django.shortcuts import render_to_response, render
from products.models import Product
# Create your views here.

def product_info(request, id):
    p = Product.object.get(id=id)

    return render_to_response('product_info.html', locals());