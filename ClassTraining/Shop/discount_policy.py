def default_policy(total_price):
    return total_price


def discount_for_perm(total_price):
    return 0.95 * total_price


def christmas_discount(total_price):
    if total_price > 100:
        return total_price - 20
    return total_price

class DiscountPolicy:
    # def __init__(self, rabat):
    #     self.rabat = rabat

    def apply_discount(self, total_price):
        return total_price


class PercentageDiscount(DiscountPolicy):
    def __init__(self, percentage_rabat):
        self.percentage_rabat = percentage_rabat

    def apply_discount(self, total_price):
        return total_price - self.percentage_rabat * total_price / 100


class AbsoluteDiscount(DiscountPolicy):
    def __init__(self, constant_rabat):
        self.constant_rabat = constant_rabat

    def apply_discount(self, total_price):
        if total_price > self.constant_rabat:
            return total_price - self.constant_rabat
        else:
          print("Too less cost of order to have discount")