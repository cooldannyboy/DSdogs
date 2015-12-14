from django.contrib import admin
from products.models import ProductCategory, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price', 'category', 'date')
    list_filter = ('stock','date')
    search_fields = ('name', 'price')

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
