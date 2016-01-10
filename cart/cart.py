from cart.models import *

CART_ID = '_CART_ID_'

class Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)

        if cart_id:
            cart_model = Cart.objects.get(id=cart_id)

    def kids(cls):
        print("count=", cls.count)

