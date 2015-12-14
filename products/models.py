from django.db import models
from datetime import date

class ProductCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    name     = models.CharField(max_length=20)
    stock    = models.IntegerField(default=0)
    price    = models.DecimalField(max_digits=4, decimal_places=0)
    date     = models.DateField(default=date.today)
    category = models.ForeignKey(ProductCategory)
    image    = models.ImageField(upload_to='products_images/')

    def __str__(self):
        return self.name
