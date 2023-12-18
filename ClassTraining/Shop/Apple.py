
class Apple:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size =size
        self.price = price

    def count_price_apple(self, amount):
        total_price = float(self.price) * int(amount)
        return total_price

    def __repr__(self):
        return f"<Apple species_name is: '{self.species_name}', size={self.size}, price={self.price}>"

from dataclasses import dataclass

@dataclass
class Apple:
    species_name: str
    size: int
    price: int

    def count_price_apple(self, amount):
        total_price = float(self.price) * int(amount)
        return total_price
    # def __repr__(self):
    #     return f"<Apple species_name is: '{self.species_name}', size={self.size}, price={self.price}>"
