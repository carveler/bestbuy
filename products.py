class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if not isinstance(name, str):
            raise TypeError("Name has to be a string.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price has to be an integer or float.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity has to be an integer.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        '''
        get_quantity(self) -> float
        Getter function for quantity.
        Returns the quantity (float).
        '''
        return float(self.quantity)

    def set_quantity(self, quantity):
        '''
        Setter function for quantity. If quantity reaches 0,
        deactivates the product.
        '''
        if quantity == 0:
            self.active = False
        self.quantity = quantity

    def is_active(self):
        '''
        Getter function for active.
        Returns True if the product is active, otherwise False.
        '''
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, {self.price}, {self.quantity}")

    def buy(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity has to be an integer.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")
        if quantity <= 0:
            raise ValueError("Quantity has to be greater than zero.")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity
