class Product:
    '''
    The Product class represents a specific type of product available in the store.
    It encapsulates information about the product,
    including its name, price, quantity, and status (active or not).
    '''

    def __init__(self, name, price, quantity):
        '''
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception.

        :param name: str - The name of the product.
        :param price: float or int - The price of the product.
        :param quantity: int - The quantity of the product.
        '''
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
        :return: float - The quantity of the product.
        '''
        return float(self.quantity)

    def set_quantity(self, quantity):
        '''
        Setter function for quantity. If quantity reaches 0,
        deactivates the product.
        :param quantity: int - The new quantity of the product.
        '''
        if quantity == 0:
            self.active = False
        self.quantity = quantity

    def is_active(self):
        '''
        Getter function for active status.
        Returns True if the product is active, otherwise False.

        :return: bool - The active status of the product.
        '''
        return self.active

    def activate(self):
        '''
        Activates the product by setting active to True.
        '''
        self.active = True

    def deactivate(self):
        '''
        Deactivates the product by setting active to False.
        '''
        self.active = False

    def show(self):
        '''
        Prints the product details (name, price, quantity).
        '''
        print(f"{self.name}, {self.price}, {self.quantity}")

    def buy(self, quantity):
        '''
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        Raises an exception if the quantity is not an integer, exceeds available stock, or is less than or equal to zero.

        :param quantity: int - The quantity to buy.
        :return: float - The total price of the purchase.
        '''
        if not isinstance(quantity, int):
            raise TypeError("Quantity has to be an integer.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")
        if quantity <= 0:
            raise ValueError("Quantity has to be greater than zero.")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity
