from django.shortcuts import render_to_response
from accounts.forms import RegistrationForm, LoginForm
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login as django_login, logout as django_logout


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.POST:
        f = LoginForm(request.POST)
    else:
        f = LoginForm()

    email = request.POST.get('email', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(email=email, password=password)

    if user is not None and user.is_active:
        django_login(request, user)
        return HttpResponseRedirect('/')
    else:
        if request.POST:
            errors_msg = 'username or password is incorrect'

        return render_to_response('registration/login.html', RequestContext(request, locals()))

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("Create registration form by POST")
        if form.is_valid():
            print("form is valid")
            user = form.save()
            # return HttpResponseRedirect('accounts/login')
            return HttpResponseRedirect('/')
            # if user is not None and user.is_active:
            #     auth.login(request, user)
            #     return HttpResponseRedirect('/')
    else:
        # form = EmailUserCreationForm()
        form = RegistrationForm()
        errors_msg = 'form create fail'

    return render_to_response('registration/register.html', RequestContext(request, locals()))

