from django.contrib import admin

from django.contrib import admin
from cart.models import Cart, Item

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')

admin.site.register(Cart, CartAdmin)
admin.site.register(Item, ItemAdmin)