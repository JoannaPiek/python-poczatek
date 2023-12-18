from Shop.Product import Product
from Shop.OrderElement import OrderElement
class TaxCalculator:
    TAX_FRUIT = 0.05
    TAX_FOOD = 0.07
    TAX_OTHER = 2
    def __init__(self, tax):
        self.tax = tax
        return tax

    @staticmethod
    def tax_calculate(positions_order):
        cathegory = positions_order.product.nazwa_kat
        if cathegory == "Owoce":
            tax = TaxCalculator.TAX_FRUIT
        elif cathegory == "Jedzenie":
            tax = TaxCalculator.TAX_FOOD
        else:
            tax = TaxCalculator.TAX_OTHER
        return tax * positions_order.count_price()

