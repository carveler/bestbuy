import products


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        '''
        Adds a product from store.
        '''
        self.products.append(product)

    def remove_product(self, product):
        '''
        Removes a product from store.
        '''
        new_products = []
        for item in self.products:
            if not product.name == item.name:
                new_products.append(item)
        self.products = new_products

    def get_total_quantity(self):
        '''
        get_total_quantity(self) -> int
        Returns how many items are in the store in total.
        '''
        total_quantity = 0
        for item in self.products:
            total_quantity += item.quantity
        return total_quantity

    def get_all_products(self):
        '''
        get_all_products(self) -> List[Product]
        Returns all products in the store that are active.
        '''
        active_products = []
        for item in self.products:
            if item.active == True:
                active_products.append(item)
        return active_products

    def order(self, shopping_list):
        '''
        order(self, shopping_list) -> float
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        '''
        total = 0
        for item in shopping_list:
            product_class, quantity = item
            total += product_class.price * quantity
        return total
