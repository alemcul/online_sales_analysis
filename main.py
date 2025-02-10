from product_manager import ProductManager
from product import Product
from cart import Cart
# Creăm instanța ProductManager
manager = ProductManager()

# Adăugăm produse
manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Telefon", 2000, 10))
manager.add_product(Product("Căști", 150, 20))
manager.add_product(Product("Maus", 160, 30))
# Afișăm produsele și valoarea totală a inventarului
manager.display_products()
print(manager.total_inventory_value())
# Testăm eliminarea unui produs
manager.remove_product("Telefon")

# Afișăm din nou lista de produse pentru a verifica eliminarea
manager.display_products()
# Creăm o instanță a coșului de cumpărături
cart = Cart()

# Selectăm 3 produse arbitrare și le adăugăm în coș
cart.add_to_cart(manager.products[0], 2)  # Adaugă 2 Laptopuri
cart.add_to_cart(manager.products[1], 1)  # Adaugă 1 Telefon
cart.add_to_cart(manager.products[2], 3)  # Adaugă 3 Căști

# Afișăm coșul și valoarea totală
cart.display_cart()
print(cart.calculate_total())
