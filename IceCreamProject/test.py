def item_list(arr):
    for i, item in enumerate(arr):
        print(f'{i + 1}. {item[0]}: {item[1]}')

def cart_price(cart):
    price = 0
    for item in cart:
        price += int(item[1])
    return price

# Ice cream counter
if __name__ == "__main__":
    cash_register = 0
    cart = []
    items = [
        ('Вафельний ріжок', 25),
        ('Цукровий ріжок', 35),
        ('Креманка', 40)
    ]

    while True:
        if len(cart) == 0:
            print('Your cart is empty now.\n')
        else:
            print(f'Your cart contains {len(cart)} items.\n')

        print(
            "Choose an option:\n"
            "  1) Вафельний ріжок\n"
            "  2) Цукровий ріжок\n"
            "  3) Креманка\n"
            "  4) Check the cash amount\n"
            "  5) Cart\n"
            "  6) Exit the application"
        )

        options = [1, 2, 3, 4, 5, 6]
        option = None

        # Checking for correct input
        while option not in options:
            try:
                option = int(input().strip())
                if option not in options:
                    print("Choose a correct option.")
            except ValueError:
                print("Please enter a valid number.")

        # Adding ice creams to the cart and updating the cash register
        if option in [1, 2, 3]:
            cart.append(items[option - 1])
            # cash_register += items[option - 1][1]

        # Check the current cash
        if option == 4:
            print(f"\nYour current cash is {cash_register}.\n")

        # Operations with the cart: Change items, clear, or buy
        if option == 5:
            cart_option = None
            while cart_option != 4:
                item_list(cart)
                print(
                    "Choose an option:\n"
                    "  1) Change items\n"
                    "  2) Clear cart\n"
                    "  3) Buy\n"
                    "  4) Go back to shopping"
                )
                try:
                    cart_option = int(input().strip())
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if cart_option == 1:
                    while True:
                        if len(cart) == 0:
                            print(' no items to remove. Back to previous page...')
                            break
                        print("\nWhat items you want to remove? (type exit to go back)\n")
                        item_list(cart)
                        answer = input('Type number of row where selected item is mentioned: ')
                        if answer == 'exit':
                            break
                        elif int(answer) in range(1, len(cart) + 1):
                            cart.pop(int(answer) - 1)
                        else:
                            print('type the correct answer')
                elif cart_option == 2:
                    cart.clear()
                    cash_register = 0
                    print("\nCart cleared!\n")
                elif cart_option == 3:
                    cash_register = cart_price(cart)
                    print(f"\nYou bought {len(cart)} items for {cash_register}.\n")
                    cart.clear()
                    break
                    # cash_register = 0
                elif cart_option == 4:
                    print("\nGoing back to shopping.\n")

        # Exit the application
        if option == options[-1]:
            exit_answer = None
            while exit_answer not in ['y', 'n']:
                exit_answer = input("Are you sure you want to exit the app? (y/n)").lower().strip()
            if exit_answer == 'y':
                print("Thank you for shopping with us!")
                break
            else:
                print("\nContinuing shopping...\n")
