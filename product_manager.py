from product import Product

class ProductManager:
    def __init__(self):
        self.products = [] 

    def add_product(self, product):
        """Adaugă un produs în lista de produse."""
        self.products.append(product)

    def display_products(self):
        """Afișează toate produsele disponibile."""
        if not self.products:
            print("Nu există produse disponibile.")
        else:
            for product in self.products:
                print(product.display_info())

    def total_inventory_value(self):
        """Calculează valoarea totală a stocului."""
        total_value = sum(product.price * product.quantity for product in self.products)
        return f"Valoarea totală a inventarului: {total_value} RON"
