class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id # int
        self.name = name # String
        self.price = price # int
        self.quantity = quantity # int

    
    def __repr__(self):
        return f"Item(ID: {self.item_id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity})"

# Create Warehouse Class
class Warehouse:
    def __init__(self):
        self.items = []  # List to store Item objects

    def addItems(self, item_id, name, price, quantity):
        for item in self.items:
            if item.item_id == item_id:
                item.quantity += quantity
                print(f"Updated quantity of {item.name} to {item.quantity}.")
                return
        new_item = Item(item_id=item_id, name=name, price=price, quantity=quantity)
        self.items.append(new_item)
        print(f"Added new item: {new_item}.")

    def removeItems(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print(f"Removed item: {item.name}.")
                return
        print(f"No item with ID {item_id} found.")

    def searchForItem(self, item_id):
        """
        Search for an item by its ID and return its details.
        """
        for item in self.items:
            if item.item_id == item_id:
                return f"Item found: {item.name}, Quantity: {item.quantity}, Price: ${item.price}"
        return f"No item with ID {item_id} found."
    
    # List all items
    def listAllItems(self, item_id):
        """
        List all items currently in the warehouse.
        """
        if not self.items:
            return "No items in the warehouse."
        
        all_items = []
        for item in self.items:
            all_items.append(f"ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}, Price: ${item.price}")
        return "\n".join(all_items)

# Test Case
warehouse = Warehouse()

# Add items
warehouse.addItems(1, "Laptop", 1500, 10)
warehouse.addItems(2, "Phone", 800, 5)
warehouse.addItems(1, "Laptop", 1500, 5)  # Update quantity for Laptop

# Remove an item
warehouse.removeItems(2)  # Remove Phone

# Try removing an item that doesn't exist
warehouse.removeItems(3)

   

# Sample Items

warehouse = Warehouse()
# Creating a sample inventory
item1 = Item(1, "Laptop", 1500, 10)
item2 = Item(2, "Phone", 800, 5)
item3 = Item(3, "Monitor", 300, 15)
item4 = Item(4, "Keyboard", 50, 20)
item5 = Item(5, "Mouse", 25, 50)
# Test case
warehouse = Warehouse()

# Add items to the warehouse
warehouse.addItems(1, "Laptop", 1500, 10)
warehouse.addItems(2, "Phone", 800, 5)
warehouse.addItems(3, "Mouse", 25, 50)

# Search for an item
print(warehouse.searchForItem(2))  # Output: Item found: Phone, Quantity: 5, Price: $800

# Search for a non-existent item
print(warehouse.searchForItem(4))  # Output: No item with ID 4 found.

# List all items
print("\nItems in Warehouse:")
print(warehouse.listAllItems(1))

