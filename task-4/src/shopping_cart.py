class ShoppingCart:

    def __init__(self):
        self.items = {}
    # In a dynamically typed World, we use hints :-(
    # Maybe then we can actually take a hint.
    def add_item(self, name: str, price: float, quantity: int = 1):
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be an integer greater than zero")

        name = name.strip()
        if name in self.items:
            # Bug: adding an existing item doubles the added quantity
            # TODO: Fix the bug.
            # Why: to make sure that the pytest is working as expected.
            self.items[name]["quantity"] += quantity * 2  
            self.items[name]["price"] = price 
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name: str, quantity: int = None):
        if not name or not isinstance(name, str):
            raise ValueError("Item name must be a non-empty string")
        
        name = name.strip()
        if name not in self.items:
            raise ValueError(f"Item '{name}' is not in the shopping cart")

        if quantity is not None:
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity to remove must be an integer greater than zero")
            
            if quantity >= self.items[name]["quantity"]:
                del self.items[name]
            else:
                self.items[name]["quantity"] -= quantity
        else:
            del self.items[name]

    def calculate_total(self) -> float:
        total = sum(item["price"] * item["quantity"] for item in self.items.values())
        return round(total, 2)

    def get_items(self) -> dict:
        return self.items

    def clear(self):
        self.items.clear()
