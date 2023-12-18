import random
from dataclasses import dataclass

# class Product:
#     def __init__(self, nazwa, nazwa_kat, price, identifier):
#         self.nazwa = nazwa
#         self.nazwa_kat = nazwa_kat
#         self.price=price
#         self.identifier = identifier
#
#     def __str__(self):
#         return f"product: {self.nazwa} z kategorii {self.nazwa_kat} i cenie jednost:{self.price}i numer id: {self.identifier}"
#
#     def __eq__(self, other):
#         if self.__class__ != other.__class__:
#             return NotImplemented
#         return (self.nazwa == other.nazwa and
#                 self.nazwa_kat == other.nazwa_kat and
#                 self.price == other.price and
#                 self.identifier == other.identifier)
#
#
# class ProductInherit(Product):
#     def __init__(self, nazwa, nazwa_kat, price, production_year, shelf_life):
#         super().__init__(nazwa,nazwa_kat,price)
#         self.production_year = production_year
#         self.shelf_life = shelf_life
#
#     def does_expire(self, curr_year):
#         left_time = int(curr_year) - int(self.production_year)
#         return left_time > int(self.shelf_life)



def create_random_amount():
    amount = random.randint(2, 40)
    print(amount)
    products = []
    for index in range(amount):
        product = f"Product+{index}"
        print(f"{product}")
        unit_price = random.randint(2, 200)
        identifier = random.randint(1,2000)
        products.append(Product(product, "food", unit_price,identifier))
    print(products)
    return products

from enum import Enum, auto

class Kategorie(Enum):
    WARZYWA = "JARZYNY"
    SLODYCZE = "SWEETS"
    WEDLINA = "MEAT"
@dataclass
class Product:
    nazwa: str
    nazwa_kat: Kategorie
    price: int
    identifier: int
    def __str__(self):
        return f"product: {self.nazwa} z kategorii {self.nazwa_kat} i cenie jednost:{self.price}i numer id: {self.identifier}"

class ProductInherit(Product):
    production_year: int
    shelf_life: int

    def does_expire(self, curr_year):
        left_time = int(curr_year) - int(self.production_year)
        return left_time > int(self.shelf_life)