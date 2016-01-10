from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from products.views import product_info
#from cart.views import

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DSdogs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/([0-9]+)', product_info),
#    url(r'^product/(.+)', product_info),
    url(r'^$', 'DSdogs.view.index'),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    # url(r'^product/cart', include('cart.urls', namespace='cart')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
