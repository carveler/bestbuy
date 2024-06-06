class Store:
    """
    The Store class represents a store that sells products.
    It manages the inventory of products and provides
    methods to add, remove, and order products.

    Attributes:
    - list_products (list): A list of Product objects
    representing the products available in the store.
    """

    def __init__(self, list_products):
        """
        Initiator (constructor) method.
        Initializes the Store object with a list of products.

        :param list_products: list - A list of Product
        objects representing the products available in the store.
        """
        self.list_products = list_products

    def add_product(self, product):
        """
        Adds a product to the store's inventory.

        :param product: Product - The Product object to add to the store.
        """
        self.list_products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store's inventory.

        :param product: Product - The Product object to remove from the store.
        """
        new_products = []
        for item in self.list_products:
            if not product.name == item.name:
                new_products.append(item)
        self.list_products = new_products

    def get_total_quantity(self):
        """
        Returns the total quantity of items in the store's inventory.

        :return: int - The total quantity of items in the store.
        """
        total_quantity = 0
        for item in self.list_products:
            total_quantity += item.quantity
        return total_quantity

    def get_all_products(self):
        """
        Returns a list of all active products in the store.

        :return: list - A list of Product objects representing
        all active products in the store.
        """
        active_products = []
        for item in self.list_products:
            if item.active is True:
                active_products.append(item)
        return active_products

    @staticmethod
    def order(shopping_list):
        """
        Processes an order based on the provided shopping list
        and returns the total price of the order.

        :param shopping_list: list - A list of tuples where
        each tuple contains a Product object and the desired quantity.
        :return: float - The total price of the order.
        """
        total = 0
        for item in shopping_list:
            product_class, quantity = item
            total += product_class.buy(quantity)
        return total

    def __contains__(self, item):
        return item in self.list_products

    def __add__(self, other):
        return self.list_products + other.list_products
