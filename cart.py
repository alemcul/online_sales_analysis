from product import Product

class Cart:
    def __init__(self):
        """Inițializează un coș de cumpărături gol."""
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        """Adaugă un produs în coș, verificând stocul."""
        if product.quantity >= quantity:
            self.cart_items.append((product, quantity))
            product.update_quantity(product.quantity - quantity)
            print(f"{quantity} x {product.name} adăugat în coș.")
        else:
            print(f"Stoc insuficient pentru {product.name}!")

    def calculate_total(self):
        """Calculează valoarea totală a coșului."""
        total = sum(product.price * quantity for product, quantity in self.cart_items)
        return f"Total de plată: {total} RON"

    def display_cart(self):
        """Afișează conținutul coșului de cumpărături."""
        if not self.cart_items:
            print("Coșul de cumpărături este gol.")
        else:
            print("Conținutul coșului:")
            for product, quantity in self.cart_items:
                print(f"{quantity} x {product.name} - {product.price} RON fiecare")
