from django.shortcuts import render_to_response
from cart.models import Cart, Item
from products.models import Product
from django.template import RequestContext
import datetime

def cart_page(request):
    cart = get_cart(request)
    items = cart.item_set.all()

    if 'del_item_id' in request.POST:
        try:
            items.get(id=request.POST['del_item_id']).delete()
        except:
            pass

    subtotal = 0
    for item in items:
        subtotal += item.total_price

    return render_to_response('cart_page.html', RequestContext(request, locals()))
    # return render_to_response('cart_page.html', locals())

CART_ID = '_DS_CART_ID_'

def get_cart(request):
    cart_id = request.session.get(CART_ID)

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except:
            cart = create_new_cart(request)
    else:
        cart = create_new_cart(request)

    return cart

def create_new_cart(request):
    cart = Cart.objects.create(created_date = datetime.datetime.now())
    request.session[CART_ID] = cart.id
    return cart

def add_to_cart(request, product, quantity, unit_price):
    cart = get_cart(request)

    try:
        item = Item.objects.get(cart=cart, product=product)
        item.quantity = item.quantity + quantity
        item.save()
    except:
        Item.objects.create(cart=cart, product=product, quantity=quantity, unit_price=unit_price)


def remove_from_cart(request, product):
    cart = get_cart(request)
    try:
        item = Item.objects.get(cart=cart, product=product)
        item.delete()
    except:
        pass

def clear_cart(request):
    cart  = get_cart(request)
    for item in cart.item_set.all():
        item.delete()

