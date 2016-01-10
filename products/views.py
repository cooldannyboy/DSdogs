from django.shortcuts import render_to_response, render
from products.models import Product
from django.template import RequestContext
# Create your views here.

def product_info(request, id):
    p = Product.objects.get(id=id)

    return render_to_response('product_info.html', RequestContext(request, locals()));

# def product_info(request, name):
#     p = Product.objects.get(name=name)
#
#     return render_to_response('product_info.html', locals());