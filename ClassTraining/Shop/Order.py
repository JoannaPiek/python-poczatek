from Shop.Product import Product
from Shop.OrderElement import OrderElement
import random
from Shop.discount_policy import DiscountPolicy, AbsoluteDiscount, PercentageDiscount


class Order:

    MAX_EL_AMOUNT = 4

    def __init__(self, name_surname, positions_order=None, discount_policy=None):
        self.name_surname = name_surname
        if positions_order is None:
            positions_order = []
        if len(positions_order) > Order.MAX_EL_AMOUNT:
            positions_order = positions_order[:Order.MAX_EL_AMOUNT]
        self._positions_order = positions_order
        if discount_policy is None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy
   #     self.total_price = self._total_order_price_count()

    def _total_order_price_count(self):
        total_price = 0
        for position in self._positions_order:
            total_price += position.count_price()
        return self.discount_policy.apply_discount(total_price)

    @property
    def total_price_order(self):
        total_price = 0
        for position in self._positions_order:
            total_price += position.count_price()
        return self.discount_policy.apply_discount(total_price)

    def add_product_to_order(self,product, quantity):
        if len(self._positions_order) >= Order.MAX_EL_AMOUNT:
            print("Limit exceeded, you can't add new product")
        else:
            new_product = OrderElement(product, quantity)
            self._positions_order.append(new_product)
            self.total_price = self._total_order_price_count()

    def __len__(self):
        return len(self._positions_order)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if len(self.positions_order) != len(other.positions_order):
            return False
        if self.name_surname != other.name_surname:
            return False
        for position in self._positions_order:
            if position not in other.positions_order:
                return False
        return True

    def __str__(self):
        mark_line = "-" * 20
        order_details = f"Zamowienie złozone przez {self.name_surname} o łąznej cenie {self.total_price_order}"
        product_details = f"zamówione pozycje:"
        for position in self._positions_order:
            product_details += f"\t{position}\n"
            # print("/t", end="")
            # position.print_self()
        mark_line_2 = "=" * 20

        result = "\n".join([mark_line, order_details, product_details, mark_line_2])
        return result

    @property
    def positions_order(self):
        return self._positions_order

    @positions_order.setter
    def positions_order_create(self, value):
        if len(value) >= Order.MAX_EL_AMOUNT:
            print("Limit exceeded, you can't add new product")
        else:
            #new_product = OrderElement(product, quantity)
            self._positions_order=value
  #      self.total_price = self._total_order_price_count()

class ExpressOrder(Order):
    EXPRESS_DELIVERY_FEE = 15

    def __init__(self, name_surname, delivery_time, positions_order=None, discount_policy=None):
        super().__init__(name_surname,positions_order,discount_policy)
        self.delivery_time = delivery_time

    # @property
    # def total_price_order(self):
    #     total_price = 0
    #     for position in self._positions_order:
    #         total_price += position.count_price()
    #     return self.discount_policy(total_price) + ExpressOrder.EXPRESS_DELIVERY_FEE

    @property
    def total_price_order(self):
        return super().total_price_order + ExpressOrder.EXPRESS_DELIVERY_FEE
    def __str__(self):
        mark_line = "-" * 20
        order_details = f"Expresowe zamowienie złozone przez {self.name_surname} o łącznej cenie {self.total_price_order}"
        delivery_details = f"Predicted delivery is on {self.delivery_time}"
        product_details = f"zamówione pozycje:"
        for position in self._positions_order:
            product_details += f"\t{position}\n"
            # print("/t", end="")
            # position.print_self()
        mark_line_2 = "=" * 20

        result = "\n".join([mark_line, order_details, delivery_details, product_details, mark_line_2])
        return result