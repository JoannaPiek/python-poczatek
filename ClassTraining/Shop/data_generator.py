from Shop.OrderElement import OrderElement
import random
from Shop.discount_policy import default_policy
from Shop.Product import Product
from Shop.Order import Order
from Shop.Product import Kategorie

MIN_QUANTITY = 2
MAX_QUANTITY = 12

MIN_UNIT_PRICE = 3
MAX_UNIT_PRICE = 17
def create_oder_position(amount=None):
    positions_order = []
    if amount is None:
        amount = random.randint(2, 8)
    for index in range(amount):
        product = f"Product+{index}"
        category_name = "Inne"
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        identifier = random.randint(1, 2000)
        product = Product(product, category_name, unit_price, identifier)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        positions_order.append(OrderElement(product, quantity))

    order = Order(name_surname="JoannaPiek", positions_order=positions_order)
    return order

def create_oder_pos(amount=None):
    positions_order = []
    if amount is None:
        amount = random.randint(1, Order.MAX_EL_AMOUNT)
    for index in range(amount):
        product = f"Product+{index}"
        category_name = "Inne"
        unit_price = random.randint(2, 200)
        identifier = random.randint(1, 2000)
        kateg = Kategorie.WARZYWA
        product = Product(product, kateg.value, unit_price, identifier)
        quantity = random.randint(2, 20)
        positions_order.append(OrderElement(product, quantity))
    return positions_order

