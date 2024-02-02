class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
            self.items[item]['price'] = price
        else:
            self.items[item] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} of {item} to cart.")
    
    def remove_item(self, item, quantity=1):
        if item in self.items:
            if quantity >= self.items[item]['quantity']:
                del self.items[item]
                print(f"Removed all instances of {item} from cart.")
            else:
                self.items[item]['quantity'] -= quantity
                print(f"Removed {quantity} of {item} from cart.")
        else:
            print(f"{item} not in cart.")
    
    def show_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item, details in self.items.items():
                print(f"{item} - Price: {details['price']} x {details['quantity']}")
    
    def calculate_total(self):
        return sum(details['price'] * details['quantity'] for item, details in self.items.items())


cart = ShoppingCart()
cart.add_item('watch', 1299, 2)
cart.add_item('pencil', 1.99)
cart.show_cart()
cart.remove_item('pencil')
cart.show_cart()
print(f"Total cost: {cart.calculate_total()}")
