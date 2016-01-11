from django.db import models
from products.models import Product

class Cart(models.Model):
    created_date = models.DateTimeField()

    def __str__(self):
        return 'Cart id='+ str(self.id) + ' crate_time='+str(self.created_date)

class Item(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=18, decimal_places=0)

    def get_total_price(self):
        return self.quantity*self.unit_price

    total_price = property(get_total_price)


# class Order(models.Model):
#     created_date = models.DateTimeField()
#     cart = models.ForeignKey(Cart)
#     user_name = models.CharField(max_length=20)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     address = models = models.CharField(max_length=255)
#     claim_paid = models.BooleanField(default=False)
#     check_paid = models.BooleanField(default=False)
#     memo = models.TextField(max_length=255, blank=True)