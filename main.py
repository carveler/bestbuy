import products
import store

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
]
best_buy = store.Store(product_list)


def show_menu():
    """
    Show Store menu
    """
    print("")
    print("   Store Menu")
    print("   ----------")
    print(
        "1. List all products in store\n"
        "2. Show total amount in store\n"
        "3. Make an order\n"
        "4. Quit\n"
    )


def ask_user():
    """
    prompt user until getting correct answer
    """
    while True:
        user_input = input("Please choose a number: ")
        if user_input in ["1", "2", "3", "4"]:
            return int(user_input)
        print("Error with your choice! Try again!")


def list_products():
    """
    list all products in store
    """
    print("")
    print("   Products in store")
    print("   -----------------")
    for i, product in enumerate(best_buy.list_products):
        print(f"{i+1}: {product}")


def show_total_amount():
    """
    show total amount in store
    """
    print("")
    print("   Total amount in store")
    print("   --------------------")
    print(f"Total amount: {best_buy.get_total_quantity()}")


def ask_user_for_product():
    """
    prompt user for product name
    :return: int or ''
    """
    while True:
        product_num = input("which product # do you want?: ")
        if product_num == "":
            return ""
        if product_num.isdigit() and int(product_num) in range(
            1, len(best_buy.list_products) + 1
        ):
            return int(product_num)
        print("Error with your choice! Try again!")


def ask_user_for_quantity(product_chosen):
    """
    prompt user for quantity
    :param product_chosen: Product
    :return: int
    """
    while True:
        quantity = input("how many do you want?: ")
        if quantity.isdigit() and int(quantity) in range(
            1, product_chosen.quantity + 1
        ):
            return int(quantity)
        print("Order quantity must be greater than zero and less than " 
              "stock.200")


def get_user_order():
    """
    prompt user for order
    :return: list of Tuple(Product, int)
    """
    new_order = []
    while True:
        user_product = ask_user_for_product()
        if user_product == "":
            break
        product_chosen = best_buy.list_products[user_product - 1]
        user_quantity = ask_user_for_quantity(product_chosen)
        new_order.append((product_chosen, user_quantity))
        if user_product == "" and user_quantity == "":
            break
    return new_order


def order_total():
    """
    make an order
    print total purchase
    :return: float
    """
    print("")
    print("   Make an order")
    print("   --------------")
    print("When you want to finish order, enter empty text.")

    try:
        new_order = get_user_order()
        for item in new_order:
            product_chosen, user_quantity = item
            print(
                f"{user_quantity} x {product_chosen.name}: "
                f"${product_chosen.price} "
            )
        total = best_buy.order(new_order)
        print(f"Order made! Total payment: ${total}")
        return total

    except ValueError as val_err:
        print(val_err)
    except TypeError as type_err:
        print(type_err)


def quit_program():
    """
    quit program
    """
    print("Bye!")
    exit()


def execute_user_choice(user_choice):
    """
    execute_user_choice
    :param user_choice: int
    """
    choice = {1: list_products, 2: show_total_amount, 3: order_total,
              4: quit_program}
    choice[user_choice]()


def start():
    """
    start program

    """
    try:
        while True:
            show_menu()
            user_input = ask_user()
            execute_user_choice(user_input)

    except ValueError as val_err:
        print(val_err)
    except TypeError as type_err:
        print(type_err)


# Create promotion catalog
second_half_price = products.SecondHalfPrice("Second Half price!")
third_one_free = products.ThirdOneFree("Third One Free!")
thirty_percent = products.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


if __name__ == "__main__":
    start()
