from dataclasses import dataclass
class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

    def count_price_potato(self, amount):
        total_price = float(self.price) * int(amount)
        return total_price

    def __repr__(self):
        return f"<Potato species_name is: '{self.species_name}', size={self.size}, price={self.price}>"

@dataclass
class Potato:
    species_name: str
    size: int
    price: int

    def count_price_potato(self, amount):
        total_price = float(self.price) * int(amount)
        return total_price

    def __repr__(self):
        return f"<Potato species_name is: '{self.species_name}', size={self.size}, price={self.price}>"