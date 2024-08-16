
import sqlite3
import time

def item_list(arr):
    """Print the items in the list with their index."""
    if not arr:
        print("Your cart is empty.")
    else:
        for i, item in enumerate(arr):
            print(f'{i + 1}. {item[0]}: {item[1]}')

def cart_price(cart):
    """Calculate the total price of items in the cart."""
    return sum(item[1] for item in cart)

def total_cash_amount(items, connection):
    """Calculate the total cash amount based on sales."""
    cash = 0
    for item_name, item_price in items:
        cursor = connection.execute('SELECT saled FROM sales WHERE item = ?', (item_name,))
        saled = cursor.fetchone()[0]
        cash += saled * item_price
    return cash

if __name__ == "__main__":
    try:
        # Set timeout and enable WAL mode
        connection = sqlite3.connect('data.db', timeout=10)
        connection.execute('PRAGMA journal_mode=WAL;')
        connection.commit()

        connection.execute('CREATE TABLE IF NOT EXISTS sales (item TEXT, price INTEGER, saled INTEGER);')
        connection.commit()

        items = [
            ('Вафельний ріжок', 25),
            ('Цукровий ріжок', 35),
            ('Креманка', 40)
        ]
        cart = []

        # Insert items into the sales table if not already present
        with connection:
            for item_name, item_price in items:
                connection.execute(
                    "INSERT INTO sales (item, price, saled) SELECT ?, ?, 0 WHERE NOT EXISTS (SELECT 1 FROM sales WHERE item = ?)",
                    (item_name, item_price, item_name)
                )

        while True:
            print(
                f"Choose an option:\n"
                f"  1) {items[0][0]}\n"
                f"  2) {items[1][0]}\n"
                f"  3) {items[2][0]}\n"
                f"  4) Check the cash amount\n"
                f"  5) Cart\n"
                f"  6) Set saled to Zero\n"
                f"  7) Exit the application"
            )

            try:
                option = int(input("Enter your choice: ").strip())
            except ValueError:
                print("Please enter a valid number.")
                continue

            if option in [1, 2, 3]:
                cart.append(items[option - 1])

            # Check for current cash
            elif option == 4:
                cash_register = total_cash_amount(items, connection)
                print(f"\nYour current cash is equal to {cash_register}\n")

            # Operations with the cart: Change items, clear, or buy
            elif option == 5:
                while True:
                    print("\nYour cart:")
                    item_list(cart)
                    print(
                        "Choose an option:\n"
                        "  1) Remove items\n"
                        "  2) Clear cart\n"
                        "  3) Buy items\n"
                        "  4) Go back to shopping"
                    )

                    try:
                        cart_option = int(input("Enter your choice: ").strip())
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    if cart_option == 1:
                        if not cart:
                            print("No items to remove. Back to previous page...")
                            break
                        item_list(cart)
                        answer = input("Type the number of the item to remove (or type 'exit' to go back): ").strip()
                        if answer.lower() == 'exit':
                            break
                        try:
                            index = int(answer) - 1
                            if 0 <= index < len(cart):
                                cart.pop(index)
                            else:
                                print("Invalid item number.")
                        except ValueError:
                            print("Please enter a valid number.")
                    elif cart_option == 2:
                        cart.clear()
                        print("\nCart cleared!\n")
                    elif cart_option == 3:
                        cash_register = cart_price(cart)
                        print(f"\nYou bought {len(cart)} items for {cash_register}.\n")

                        # Update the database with cart values
                        try:
                            with connection:
                                for item in cart:
                                    connection.execute(
                                        "UPDATE sales SET saled = saled + 1 WHERE item = ?",
                                        (item[0],)
                                    )
                        except sqlite3.OperationalError as e:
                            if 'database is locked' in str(e):
                                print("Database is locked, retrying...")
                                time.sleep(1)
                                continue

                        # Clear the cart after committing
                        cart.clear()
                        break
                    elif cart_option == 4:
                        print("\nGoing back to shopping.\n")
                        break
                    else:
                        print("Invalid option.")

            # Set saled values to zero
            elif option == 6:
                exit_answer = None
                while exit_answer not in ['y', 'n']:
                    exit_answer = input("Are you sure you want to set values to zero? (y/n) ").lower().strip()
                if exit_answer == 'y':
                    try:
                        with connection:
                            connection.execute('UPDATE sales SET saled = 0')
                        print("\nAll 'saled' values have been set to zero.\n")
                    except sqlite3.OperationalError as e:
                        if 'database is locked' in str(e):
                            print("Database is locked, retrying...")
                            time.sleep(1)
                            continue

            # Exit from application
            elif option == 7:
                exit_answer = None
                while exit_answer not in ['y', 'n']:
                    exit_answer = input("Are you sure you want to exit the app? (y/n) ").lower().strip()
                if exit_answer == 'y':
                    print("Thank you for shopping with us!")
                    break
            else:
                print("Invalid option.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        print("\nProcess was interrupted. Exiting gracefully.")
    finally:
        if connection:
            connection.close()
        print("Database connection closed.")
 
