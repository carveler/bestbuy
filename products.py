from abc import ABC, abstractmethod


class Product:
    """
    The Product class represents a specific type of product available
    in the store.
    It encapsulates information about the product,
    including its name, price, quantity, and status (active or not).
    """

    def __init__(
        self,
        name,
        price,
        quantity=0,
        promotion=None,
    ):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity),
        raises an exception.

        :param name: str - The name of the product.
        :param price: float or int - The price of the product.
        :param quantity: int - The quantity of the product.
        :param promotion: Promotion - The promotion to apply to the product
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
        self._price = float(price)
        self._quantity = quantity
        self.active = True
        self._promotion = promotion

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Product price cannot be negative.")
        if not isinstance(value, int):
            raise TypeError("price has to be an integer.")
        self._price = value

    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        if not isinstance(value, Promotion) and value is not None:
            raise TypeError("Promotion has to be of type Promotion or None.")
        self._promotion = value

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

    def __str__(self):
        """
        Prints the product details (name, price, quantity, promotion).
        """

        return (
            f"Name: {self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}, Promotion: {self.promotion}"
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
        self.quantity -= value
        if self.promotion:
            if isinstance(self.promotion, PercentDiscount):
                return self.promotion.apply_promotion(
                    self, value, self.promotion.percent
                )
            else:
                return self.promotion.apply_promotion(self, value)
        else:
            return self.price * value

    def set_promotion(self, promotion):
        """
        Sets the promotion for the product.

        :param promotion: Promotion - The promotion to apply to the product.
        """
        self.promotion = promotion

    def __lt__(self, other):
        """
        <  (less than)
        """
        return self.price < other.price

    def __gt__(self, other):
        """
        > (greater than)
        """
        return self.price > other.price


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

    def __str__(self):
        """
        Prints the product details (name, price, quantity, promotion).
        """

        return (
            f"Name:{self.name}, Price:{self.price}, "
            f"Quantity:{self.quantity}, Promotion:{self.promotion}"
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
        if value <= 0:
            raise ValueError("Quantity has to be greater than zero.")
        if self.promotion:
            if isinstance(self.promotion, PercentDiscount):
                return self.promotion.apply_promotion(self, value)
            else:
                return self.promotion.apply_promotion(self, value)
        else:
            return self.price * value


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
        if self.promotion:
            if isinstance(self.promotion, PercentDiscount):
                return self.promotion.apply_promotion(
                    self, value, self.promotion.percent
                )
            else:
                return self.promotion.apply_promotion(self, value)
        else:
            return self.price * value


class Promotion(ABC):
    """
    instance variable (member) for name, and only one method:
    """

    def __init__(self, name, percent=None):
        self.name = name
        self.percent = percent

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

    def __str__(self):
        """
        Prints the product promotion.
        """
        text = f"{self.name} "
        if self.percent:
            text += f"Percent: {self.percent}"
        return text


class SecondHalfPrice(Promotion):
    """
    SecondHalfPrice applies a promotion where
    every second product is half-price.
    """

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Apply the second half-price promotion to the given product quantity.
        
        :param self:
        :param product: The product to apply the promotion to.
        :param quantity: The quantity of the product being purchased.
        :return: The total price after applying the promotion.
        """
        pair = quantity // 2
        reminder = quantity % 2
        return float(product.price * pair * 1.5 + product.price * reminder)


class ThirdOneFree(Promotion):
    """
    ThirdOneFree applies a promotion where every third product is free.
    """

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Apply the third one free promotion to the given product quantity.

        :param self:
        :param product: The product to apply the promotion to.
        :param quantity: The quantity of the product being purchased.
        :return: float The total price after applying the promotion.
        """

        three_pair = quantity // 3
        reminder = quantity % 3
        return float(product.price * three_pair * 2 + product.price * reminder)


class PercentDiscount(Promotion):
    """
    PercentDiscount applies a percentage discount
    to the total price of the products.
    """

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Apply the percentage discount to the total price of
        the given product quantity.

        :param self:
        :param product: The product to apply the promotion to.
        :param quantity: The quantity of the product being purchased.
        :return: The total price after applying the discount.
        """
        return float(product.price * quantity * (1 - self.percent / 100))
