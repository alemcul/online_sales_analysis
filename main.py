from product_manager import ProductManager
from product import Product

# Creăm instanța ProductManager
manager = ProductManager()

# Adăugăm produse
manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Telefon", 2000, 10))
manager.add_product(Product("Căști", 150, 20))

# Afișăm produsele și valoarea totală a inventarului
manager.display_products()
print(manager.total_inventory_value())
# Testăm eliminarea unui produs
manager.remove_product("Telefon")

# Afișăm din nou lista de produse pentru a verifica eliminarea
manager.display_products()
