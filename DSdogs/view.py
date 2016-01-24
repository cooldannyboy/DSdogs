#from django.http import
from django.shortcuts import render_to_response
from products.models import Product
from cart.views import add_to_cart, get_cart
from django.template import RequestContext

from django.http import HttpResponse, HttpResponseRedirect
# from DSdogs.form import LoginForm
# from django.contrib import auth
# from django.contrib.auth.forms import UserCreationForm
# from DSdogs.form import EmailUserCreationForm, RegistrationForm
# from accounts.forms import RegistrationForm
# from django.contrib.auth import login as django_login, logout as djnago_logout

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
            quantity = int(request.POST['select_quantity'])
        except:
            quantity = 1

        add_to_cart(request, product=product, quantity=quantity, unit_price=product.price)
        product_name = product.name

    else:
        pass

    return render_to_response('index.html', RequestContext(request, locals()));


# def login(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/')
#
#     if request.POST:
#         f = LoginForm(request.POST)
#     else:
#         f = LoginForm()
#
#     email = request.POST.get('email', '')
#     password = request.POST.get('password', '')
#
#     user = auth.authenticate(email=email, password=password)
#
#     if user is not None and user.is_active:
#         django_login(request, user)
#         return HttpResponseRedirect('/')
#     else:
#         if request.POST:
#             errors_msg = 'username or password is incorrect'
#
#         return render_to_response('registration/login.html', RequestContext(request, locals()))
#
# def logout(request):
#     django_login(request)
#     return HttpResponseRedirect('/')
#
# def register(request):
#     if request.method == 'POST':
#         form = EmailUserCreationForm()
        # form = RegistrationForm(request.POST)
        # print("Create registration form by POST")
        # if form.is_valid():
        #     print("form is valid")
        #     user = form.save()
        #     return HttpResponseRedirect('accounts/login')
            # return HttpResponseRedirect('/')
            # if user is not None and user.is_active:
            #     auth.login(request, user)
            #     return HttpResponseRedirect('/')
    # else:
        # form = RegistrationForm()
        # errors_msg = 'form create fail'
    #
    # return render_to_response('registration/register.html', RequestContext(request, locals()))
