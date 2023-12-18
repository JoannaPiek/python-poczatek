# class OrderElement:
#     def __init__(self, product, quantity):
#         self.product = product
#         self.quantity = quantity
#
#     def count_price(self):
#         total_price = self.quantity * self.product.price
#         return total_price
#
#     def __str__(self):
#         return f"{self.product} x {self.quantity}"
#
#     def __eq__(self, other):
#         if self.__class__ != other.__class__:
#             return NotImplemented
#         return self.product == other.product and self.quantity == other.quantity

from dataclasses import dataclass
from Shop.Product import Product
@dataclass
class OrderElement:
    product: Product
    quantity: int

    def count_price(self):
        total_price = self.quantity * self.product.price
        return total_price

    def __str__(self):
         return f"{self.product} x {self.quantity}"