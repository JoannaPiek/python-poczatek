list_of_products = {
    "apple" : {
        "ilosc" : 100,
        "cena" : 5
    },
    "bread" : {
        "ilosc" : 300,
        "cena" : 7
    }
}

def update_stock(product, ordered_amount):
    list_of_products[product]["ilosc"] -= ordered_amount