from django.conf.urls import patterns, include, url
from cart.views import cart_page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DSdogs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'$', cart_page),
)
