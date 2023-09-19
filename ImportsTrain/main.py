from Products.OrderProduct import order_products
from Products.ProductsData import update_stock

def run_shop()
    print("Sklep")
    product_name = input("Cochesz kupić:")
    amount = int(input("Podaj ilość: "))

    new_order = order_products(product_name,amount)
    if new_order is not None:
        total_price = new_order["cena"]
        print(f"ŁĄczny koszt to {total_price}")
    update_stock(product_name, amount)

if __name__ == 'main':
    run_shop()

