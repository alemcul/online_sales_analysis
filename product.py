class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Afișează informațiile despre produs."""
        return f"Produs: {self.name}, Preț: {self.price} RON, Cantitate: {self.quantity}"

    def update_quantity(self, new_quantity):
        """Actualizează cantitatea produsului."""
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Cantitatea nu poate fi negativă!")
