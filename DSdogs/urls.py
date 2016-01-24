from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from products.views import product_info
# from django.contrib.auth.views import login, logout
# from DSdogs.view import login, logout, register
from accounts.admin import admin_site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DSdogs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/([0-9]+)', product_info),
    url(r'^$', 'DSdogs.view.index'),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^accounts/', include('accounts.url', namespace='accounts')),
    url(r'myadmin/', include(admin_site.urls)),

    # url(r'^accounts/login$', login),
    # url(r'^register$', register),
    # url(r'^accounts/logout$', logout),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

