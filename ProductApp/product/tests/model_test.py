import json
from unittest import TestCase

from django.test import TestCase

from django.contrib.auth.models import User
from product.models import Product, PlaceOrder



class BaseTestClass(TestCase):
    """
    Common base class of test cases.
    """
    def setUp(self):
        self.user = User.objects.create(username='testuser',
                        email="testuseremail",
                        password="testuser123")

        self.user.set_password(self.user.password)
        self.user.save()

        self.product_one = Product.objects.create(
            symbol="TKC^17^18", 
            description="Kolano hamb. DN 10/17.2*1.8 S235 P237TR1/TR2 EN 10240-1(2) A,3,1",
            unit='SZT', 
            created_by=self.user)


class ProductTestCase(BaseTestClass):

    def test_create_product_record(self):
        """Test a product record created."""
        product = Product.objects.create(
            symbol="TKC^17^18", 
            description="Kolano hamb. DN 10/17.2*1.8 S235 P237TR1/TR2 EN 10240-1(2) A,3,1",
            unit='SZT', 
            created_by=self.user)

        self.assertEqual(product.symbol, "TKC^17^18")



class PlaceOrderTestCase(BaseTestClass):
    """
    Test case for check place order create or not.
    """
    def test_create_product_place_order(self):
        """Test a product record created."""
        place_order = PlaceOrder.objects.create(
            quantity=20, 
            product_order_by=self.user,
            product=self.product_one, 
        )

        self.assertEqual(place_order.quantity, 20)
        self.assertEqual(place_order.product.symbol, "TKC^17^18")

