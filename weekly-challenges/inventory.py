#Create a class for the inventory item, with the following attributes: name, quantity, and price.

class Inventory_item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.quantity}, {self.price}"

#Create a class for the inventory management system, with the following methods:
#add_item: allows the user to add a new item to the inventory
#remove_item: allows the user to remove an item from the inventory
#update_item: allows the user to update the quantity or price of an item
#display_inventory: displays the current inventory

class Inventory_management:
    def __init__(self):
        self.inventory = {}
    
    def add_item(self,name,quantity,price):
        if name in self.inventory:
            print("Item already Exists!")
        else:
            self.inventory[name] = Inventory_item(name,quantity, price)

inventory_obj = Inventory_management()

inventory_obj.add_item("Flour", 100, 70)
print(inventory_obj.inventory["Flour"].quantity)
