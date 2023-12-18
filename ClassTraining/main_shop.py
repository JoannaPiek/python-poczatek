from Shop.Order import Order, ExpressOrder
from Shop.Product import Product, create_random_amount, ProductInherit
from Shop.Apple import Apple
from Shop.Potato import Potato
from Shop.OrderElement import OrderElement
from Shop.tax_calculator import TaxCalculator
from Shop.discount_policy import christmas_discount, PercentageDiscount, AbsoluteDiscount
from Shop.discount_policy import discount_for_perm
import random
from Shop.data_generator import create_oder_position
from Shop.data_generator import create_oder_pos
from Shop.delivery import products_delivery

# list_order = [Order(), Order(), Order()]
    #
    # dict_product = {apple_first:Apple(), potato_first:Potato()}

def run_homework1():
    big_order = create_random_amount()
    order_final = Order("Kasia Kowal", big_order)
    order_final.print_self()

def run_homework2():
    green_apple = Apple(species_name = "Green apple", size="M", price = "1.5")
    print(f"10kg zielonego jabla kosztuje {green_apple.count_price_apple(10)}")
    old_potato = Potato(species_name="old", size="S", price="2.3")
    print(f"11kg old potato kosztuje {old_potato.count_price_potato(11):.2f}")

def run_homework3():
    first_order = create_oder_position()
    print(first_order)


def run_homework4():
    green_apple = Apple(species_name = "Green apple", size="M", price = "1.5")
    print(green_apple)
    old_potato = Potato(species_name="old", size="S", price="2.3")
    print(old_potato)


def run_homework5():
    first_order = create_oder_position()
    print(f"Liczba el w zamówieniu to: {len(first_order)}")

def run_homework6():
    cookie = Product(nazwa="ciastko", nazwa_kat="słodycze", price= 4)
    juice = Product(nazwa="sok", nazwa_kat="napoje", price= 23)
    firdt_order_el = [OrderElement(product=cookie, quantity=7), OrderElement(product=juice, quantity=3)]
    sevond_order_ek = [OrderElement(product=cookie, quantity=3), OrderElement(product=juice, quantity=8)]
    firdt_ord = Order(name_surname="JoanPiek", positions_order=firdt_order_el)
    sec_ord = Order(name_surname="AniaPiek", positions_order=sevond_order_ek)

    if firdt_ord == sec_ord:
        print("Zamowienia są jednakowe")
    else:
        print("Zamówiena są inne")


def run_homework7():
    first_order = create_oder_position()
    print(first_order)

    cookies = Product(nazwa="ciastko", nazwa_kat="słodycz", price=7 )
    first_order.add_product_to_order(cookies, 9)
    print(first_order)

def run_homework8():
    over_limit = Order.create_oder_position(8)
    print(over_limit)

    cookies = Product(nazwa="ciastko", nazwa_kat="słodycz", price=7 )
    below_limit = Order.create_oder_position(3)
    below_limit.add_product_to_order(cookies, 9)
    print(below_limit)
    over_limit.add_product_to_order(cookies, 5)
    print(over_limit)

def run_homework9():
    over_limit = Order.create_oder_position(8)
    print(over_limit)

    cookies = Product(nazwa="ciastko", nazwa_kat="Jedzenie", price=7 )
    ten_cookies = OrderElement(cookies, 10)
    tax_for_cookies = TaxCalculator.tax_calculate(ten_cookies)
    print(f"Cena ciastek za 10 sztuk to: {ten_cookies.count_price()} plus podatek {tax_for_cookies:.2f}")


def get_order_price(order):
    return order.total_price
def run_homework10():
    orders = []
    for _ in range(5):
        orders.append(Order.create_oder_position())

    orders.sort(key = lambda order: order.total_price)
    for order in orders:
        print(order)




def run_homework11():
    order_elements = create_oder_pos()
    order1 = Order(name_surname="JoannaPiek", positions_order= order_elements, discount_policy=discount_for_perm)
    order2 = Order(name_surname="JoannaPiek", positions_order=order_elements, discount_policy=christmas_discount)
    order3 = Order(name_surname="JoannaPiek", positions_order=order_elements)
    print(order1)
    print(order2)
    print(order3)

def run_homework12():
    order_elements = create_oder_pos(11)
    order1 = Order(name_surname="Asia", positions_order=order_elements)
    for el in order1.positions_order:
        print(el)

def run_homework13():
    order_elements = create_oder_pos(5)
    order1 = Order(name_surname="Asia", positions_order=order_elements)
    order2_elements = create_oder_pos(30)
    order1.positions_order_create = order2_elements
    for el in order1.positions_order:
        print(el)
    print(order1.total_price_order)


def run_homework14():
    product = ProductInherit(nazwa="pomidor", nazwa_kat="warzywa", price=567, production_year=2020, shelf_life=3)
    print(product.does_expire(2024))

def run_homework15():
    order_elements = create_oder_pos(5)
    order1 = ExpressOrder(name_surname="Kowalski", delivery_time="12-04-2024", positions_order=order_elements)
    print(order1)


def run_homework16():
    order_elements = create_oder_pos(5)
    dis_rabat_perc = PercentageDiscount(percentage_rabat=10)
    dis_rabat_quote = AbsoluteDiscount(constant_rabat=20)
    order1 = Order(name_surname="JoannaPiek", positions_order= order_elements)
    order2 = Order(name_surname="JoannaPiek", positions_order=order_elements, discount_policy=dis_rabat_perc)
    order3 = Order(name_surname="JoannaPiek", positions_order=order_elements, discount_policy=dis_rabat_quote)
    print(order1)
    print(order2)
    print(order3)

def run_homework17():
    order_elements = create_oder_pos(5)
    order1 = ExpressOrder(name_surname="Kowalski", delivery_time="12-04-2024", positions_order=order_elements)
    print(order1)


def homework18():
    order_elements = create_oder_pos()
    positions_order_dict = {order_element.product.identifier: order_element.product for order_element in order_elements}
    print(positions_order_dict)
    positions_order_dict_new = {identifier+1: product for identifier, product in positions_order_dict.items()}
    print(positions_order_dict_new)
    positions_order_dict.update(positions_order_dict_new)
    print(positions_order_dict)

def homework19():
    needed_products=[
            "chleb",
            "ciastka",
            "jabłka",
            "dżem",
            "pomarańcze",
            "marchew",
            "bułki",
            "ziemniaki",
            "ser",
            "mleko"
                 ]
    received_products = []

    while not set(needed_products) == set(received_products):
        new_products = products_delivery()
        received_products += new_products
        print(f"Przywieziono: {received_products}")
        missing_prod = set(needed_products).difference(received_products)
        print(f"Brakuje nam jeszcz {missing_prod}")

    print(f"Łącznie otrzzymano: {received_products}")


### homework for frozenset

def create_set_with_new_set(numbers):
    number = random.randint(0,10)
    numbers.add(number)
    return numbers

def create_frozenset_with_new_frozenset(numbers):
    number = random.randint(0,10)
    return numbers.union({number})

def run_function_for_set():
    numbers = set()
    while len(numbers) < 11:
        create_set_with_new_set(numbers)
        print(numbers)


def run_function_for_frozenset():
    numbers = frozenset()
    results = []

    while len(numbers) < 11:
        print(numbers)
        numbers = create_frozenset_with_new_frozenset(numbers)
      #  create_frozenset_with_new_frozenset(numbers)
        results.append(numbers)
    print(results)

###test dla tuple

def test_products_eq():
    parameters = [
        ("pomidor", "warzywa", "identifier", 24, "pomidor", "warzywa","identifier", 24, True),
        ("pomidor", "warzywa","identifier", 24, "pomidor", "słodycze","identifier", 24, False),
        ("pomidor", "warzywa","identifier", 24, "chleb", "słodycze","identifier", 24, False),
        ("pomidor", "warzywa","identifier", 24, "pomidor", "słodycze","identifier", 7, False)

    ]

    for element in parameters:
        eproduct, kategoria, cena, ident, eproduct_other, kat_other, cena_other, ident_other, expected_result = element

        result = Product(eproduct, kategoria, cena, ident) == Product(eproduct_other, kat_other, cena_other, ident_other)

        if result == expected_result:
            print(f"Test passed")
        else:
            print(f"Dla danych {element} wynik powinien byc {expected_result}, a jest {result}")


def run_test():
    test_products_eq()


##zadanie dla namedtuple
from collections import namedtuple

Appletuple = namedtuple("Appletuple", ["species_name", "size", "price"])

def run_homework():
    apple_instance_tuple = Appletuple("kortland", 15, "12zł")
    print(apple_instance_tuple.species_name, apple_instance_tuple.size, apple_instance_tuple.price)
    print(apple_instance_tuple[0], apple_instance_tuple[1], apple_instance_tuple[2])

    for element in apple_instance_tuple:
        print(element)


#dataclass homework

def dataclass_homework():
    kort_apple = Apple(species_name="kortland",size=12,price=2)
    print(kort_apple.species_name, kort_apple)

    irga = Potato(species_name="irga", size=45, price=1.2)
    print(irga.price, irga)

def dataclass_homework_2():
    product1 = Product(nazwa="pomidor", nazwa_kat="warzywo", price=2.4, identifier=123456)
    print(product1)
    order_elemnts1 = create_oder_pos(5)
    print(order_elemnts1)
    order1 = Order(name_surname="jan kowal", positions_order=order_elemnts1, discount_policy=None)
    print(order1)

#enum homework
from Shop.Product import Kategorie
def enum_homework():
    kateg = Kategorie.WARZYWA
    product2 = Product(nazwa="pomidor", nazwa_kat=kateg.value, price=2.3, identifier=345234)
    print(product2)
    order_elemnts1 = create_oder_pos(5)
    print(order_elemnts1)
    order1 = Order(name_surname="jan kowal", positions_order=order_elemnts1, discount_policy=None)
    print(order1)

if __name__ == '__main__':
    enum_homework()