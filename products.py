class Product:
    """
    The Product class represents a specific type of product available
    in the store.
    It encapsulates information about the product,
    including its name, price, quantity, and status (active or not).
    """

    def __init__(self, name, price, quantity=0):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity),
        raises an exception.

        :param name: str - The name of the product.
        :param price: float or int - The price of the product.
        :param quantity: int - The quantity of the product.
        """
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
        self._quantity = quantity
        self.active = True

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Product quantity cannot be negative.")
        if not isinstance(value, int):
            raise TypeError("Quantity has to be an integer.")
        self._quantity = value
        if self._quantity == 0 and not isinstance(self, NonStockedProduct):
            self.deactivate()

    def get_quantity(self):
        """
        get_quantity(self) -> float
        Getter function for quantity.
        Returns the quantity (float).
        :return: float - The quantity of the product.
        """
        return float(self.quantity)

    def is_active(self):
        """
        Getter function for active status.
        Returns True if the product is active, otherwise False.

        :return: bool - The active status of the product.
        """
        return self.active

    def activate(self):
        """
        Activates the product by setting active to True.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product by setting active to False.
        """
        self.active = False

    def show(self):
        """
        Prints the product details (name, price, quantity).
        """
        print(f"{self.name}, {self.price}, {self.quantity}")

    def buy(self, value):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        Raises an exception if the quantity is not an integer,
        exceeds available stock, or is less than or equal to zero.

        :param value: int - The quantity to buy.
        :return: float - The total price of the purchase.
        """
        if not isinstance(value, int):
            raise TypeError("Quantity has to be an integer.")
        if value > self.quantity:
            raise ValueError("Not enough stock available.")
        if value <= 0:
            raise ValueError("Quantity has to be greater than zero.")
        self.quantity -= value
        return self.price * value


class NonStockedProduct(Product):
    """
    the quantity should be set to zero always
    """

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    @property
    def quantity(self):
        return 0

    @quantity.setter
    def quantity(self, value):
        raise AttributeError("NonStockedProduct quantity cannot be modified.")

    def show(self):
        """
        Prints the product details (name, price, quantity).
        """

        print(
            f"{self.name} (Non-Stocked), Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )


class LimitedProduct(Product):
    """
    shipping fee can only be added once.
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """
        Prints the product details (name, price, quantity).
        """
        print(
            f"{self.name}, {self.price}, {self.quantity},"
            f" Limited item only possible to add {self.maximum} item"
        )

    def buy(self, value):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        Raises an exception if the quantity is not an integer,
        exceeds available stock, or is less than or equal to zero.

        :param value: int - The quantity to buy.
        :return: float - The total price of the purchase.
        """
        if not isinstance(value, int):
            raise TypeError("Quantity has to be an integer.")
        if value > self.quantity:
            raise ValueError("Not enough stock available.")
        if value <= 0:
            raise ValueError("Quantity has to be greater than zero.")
        if value > self.maximum:
            raise ValueError(f"{self.name} is limited to "
                             f"add max {self.maximum}.")
        self.quantity -= value
        return self.price * value
