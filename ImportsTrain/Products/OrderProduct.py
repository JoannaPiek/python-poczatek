from .ProductsData import list_of_products

orders = [{
    "product_name" : "chleb",
    "ilość" : "5",
    "cena" : "20"
}]

def order_products(prod_name, quantity_ordered):
    #for product_name in list_of_products:
     #   name = list_of_products[product_name]
      #  if name == prod_name:
    quantity = int(list_of_products[prod_name]["ilosc"])
    price = int(list_of_products[prod_name]["cena"])
    if quantity_ordered < quantity:
        total_price = quantity_ordered * price
    else:
        print(f"Quantity which you'd like to order {quantity_ordered} is more than this on stock")
        return None
    new_order = {
        "product_name": prod_name,
        "ilość": quantity_ordered,
        "cena": total_price
    }
    return new_order
    orders.append(new_order)
