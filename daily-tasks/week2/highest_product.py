products = [
    {"name": "Laptop", "price": "12000"},
    {"name": "Home Theatre System", "price": 7500},
    {"name": "Smart TV 65inches", "price": 144000},
    {"name": "Fridge Double Door", "price": 120000}
   
]

def find_highest_priced_product(products):
    for product in products:
        highest_price = 0
        if highest_price > product["price"]:
            highest_price = product["price"]
            highest_priced_product = product["name"]
    return highest_priced_product

find_highest_priced_product(products)