import products
import store

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)


def show_menu():
    print("   Store Menu")
    print("   ----------")
    print(
        "1. List all products in store\n"
        "2. Show total amount in store\n"
        "3. Make an order\n"
        "4. Quit\n"
    )


def ask_user():
    while True:
        user_input = input("Please choose a number: ")
        if user_input in ["1", "2", "3", "4"]:
            return int(user_input)
        else:
            print("Error with your choice! Try again!")
       


def start():
    try:
        show_menu()
        ask_user()

    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    start()
