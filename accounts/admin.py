from django.contrib import admin
from accounts.models import CustomerUser

class CustomerUserAdmin(admin.ModelAdmin):
    pass

class MyAdminSite(admin.AdminSite):
    site_header = 'DSdogs administraion'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(CustomerUser)

# admin.site.register(CustomerUser, CustomerUserAdmin)
