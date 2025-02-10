from product_manager import ProductManager
from product import Product
from cart import Cart

# Creăm instanța managerului de produse
manager = ProductManager()

# Adăugăm produse
manager.add_product(Product("Ultrabook", 4000, 4))
manager.add_product(Product("Smartphone", 2200, 8))
manager.add_product(Product("Căști wireless", 200, 15))

# Creăm instanța coșului de cumpărături
cart = Cart()

# Adăugăm produse în coș
cart.add_to_cart(manager.products[0], 1)
cart.add_to_cart(manager.products[1], 2)
cart.add_to_cart(manager.products[2], 1)

# Afișăm coșul și totalul de plată
cart.display_cart()
print(cart.calculate_total())
