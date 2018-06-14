from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    """
    It's product model to store the information of the product records.
    """
    SZT = 'SZT'

    UNIT_CHOICES = (
        (SZT, 'SZT'),
    )

    symbol = models.CharField(max_length=52, verbose_name='Symbol')
    description = models.TextField(verbose_name='Product Description')
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES, default=SZT, verbose_name='Unit' )

    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    created_by = models.ForeignKey(User, related_name='products')

    def __str__(self):
        return self.symbol


class PlaceOrder(models.Model):
    quantity = models.IntegerField(verbose_name='Quantity', null=True, blank=True)
    product_order_by = models.ForeignKey(User, related_name="product_orders")
    product = models.ForeignKey(Product, related_name="place_orders")

    created_date = models.DateTimeField(auto_now_add=True, verbose_name="created date")

    def __str__(self):
        return '{0} :: {1}'.format(self.quantity, self.product_order_by.username)

