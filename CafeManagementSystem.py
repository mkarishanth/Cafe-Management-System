'''
Central Perk Smart Cafe Management System
Module: Fundamentals in Programming (FIP)
'''

# -------------------- MENU DATA -------------------- #

MENU = {
    "Coffee": 350,
    "Sandwich": 550,
    "Pastry": 300,
    "Juice": 400,
    "Tea": 250
}


# -------------------- FUNCTIONS -------------------- #

def display_menu():
    # Displays the cafe menu.
    print("\n--- Central Perk Menu ---")
    for item in MENU:
        print(item, "- LKR", MENU[item])
    print("-------------------------")


def take_order():

    #Takes customer order and quantities.

    order = {}

    while True:
        item = input("Enter item name (or 'done' to finish): ").title()

        if item == "Done":
            break

        if item not in MENU:
            print("Invalid item. Please select from menu.")
            continue

        quantity = input("Enter quantity: ")

        if not quantity.isdigit():
            print("Quantity must be a number.")
            continue

        quantity = int(quantity)

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if item in order:
            order[item] = order[item] + quantity
        else:
            order[item] = quantity

    return order


def calculate_subtotal(order):
    #Calculates subtotal
    subtotal = 0
    for item in order:
        subtotal = subtotal + (MENU[item] * order[item])
    return subtotal


def apply_discount(subtotal):
    #Applies 10% discount if subtotal > 2000
    if subtotal > 2000:
        return subtotal * 0.10
    else:
        return 0


def search_item():
    #Searches menu item
    item = input("Enter item name to search: ").title()

    if item in MENU:
        print(item, "price is LKR", MENU[item])
    else:
        print("Item not available.")


def sort_menu():
    #Sorts menu
    print("1. Sort Alphabetically")
    print("2. Sort by Price")
    choice = input("Choose option: ")

    if choice == "1":
        for item in sorted(MENU):
            print(item, "- LKR", MENU[item])

    elif choice == "2":
        sorted_menu = sorted(MENU.items(), key=lambda x: x[1])
        for item, price in sorted_menu:
            print(item, "- LKR", price)

    else:
        print("Invalid choice.")


def print_receipt(order, subtotal, discount):
    #Prints receipt
    print("\n--- Receipt ---")

    for item in order:
        price = MENU[item]
        quantity = order[item]
        total = price * quantity
        print(item, "x", quantity, "= LKR", total)

    print("----------------")
    print("Subtotal :", subtotal)
    print("Discount :", discount)
    print("Total    :", subtotal - discount)
    print("----------------")


# -------------------- MAIN PROGRAM -------------------- #

def main():
    #Main control function
    while True:
        print("\n--- Central Perk Smart Cafe ---")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. Search Item")
        print("4. Sort Menu")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            display_menu()
            order = take_order()

            if len(order) == 0:
                print("No items ordered.")
            else:
                subtotal = calculate_subtotal(order)
                discount = apply_discount(subtotal)
                print_receipt(order, subtotal, discount)

        elif choice == "3":
            search_item()

        elif choice == "4":
            sort_menu()

        elif choice == "5":
            print("Thank you! Visit again.")
            break

        else:
            print("Invalid option. Try again.")


# -------------------- RUN PROGRAM -------------------- #


if __name__ == "__main__":
    main()