from django.db import models

class Cart(models.Model):
    created_date = models.DateTimeField()

    def __str__(self):
        return self.created_date

class Item(models.Model):
    cart = models.ForeignKey(Cart)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=18, decimal_places=0)

