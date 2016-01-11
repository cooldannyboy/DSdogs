#from django.http import
from django.shortcuts import render_to_response
from products.models import Product
from cart.views import add_to_cart, get_cart
from django.template import RequestContext

def context_proc(request):
    cart = get_cart(request)
    items_count = 0
    for item in cart.item_set.all():
        items_count += item.quantity

    return {'cart_items_count' : items_count}

def index(request):
    products = Product.objects.all
    cart = get_cart(request)

    if 'product_id' in request.POST:
        id = request.POST['product_id']
        product = Product.objects.get(id=id)

        try:
            quantity = request.POST['select_quantiyt']
        except:
            quantity = 1

        add_to_cart(request, product=product, quantity=quantity, unit_price=product.price)
        product_name = product.name

    else:
        pass


    return render_to_response('index.html', RequestContext(request, locals()));
