from django.conf.urls import patterns, url
from accounts.views import register, login, logout

urlpatterns = patterns('',
    # url(r'^register$', 'accounts.views.register', name='register'),
    # url(r'^login$', 'accounts.views.login', name='login'),
    # url(r'^logout$', 'accounts.views.logout', name='logout'),
    url(r'^register$', register),
    url(r'^login$', login),
    url(r'^logout$', logout),
)
