"""Collect order for a Pizza Company."""
# Validations were imported from a different
from Validations import validate_one_char, validate_string, validate_integer


def get_integer(m):
    """Request integer user input.

    :param m: str
    :return: int
    """
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    """Request string user input.

    :param m: str
    :return: str
    """
    my_string = input(m)
    return my_string


def review_menu(m):
    """Review the pizza menu.

    :param m: str
    :return: None
    """
    print("Pizza Menu")
    print("-" * 10)
    for i in range(0, len(m)):
        output = "{:^15} --- ${}".format(m[i][0], m[i][1])
        print(output)


def review_order(o):
    """Review the pizza order.

    :param o: str
    :return: None
    """
    if len(o) != 0:
        print("The customer has ordered: ")
        for i in range(0, len(o)):
            # Formats number and the name of the pizza in this output.
            # Number, Name of the pizza
            output = "{:12} {} Pizzas --- ${}".format(o[i][0],
                                                      o[i][1], o[i][2])
            print(output)
    else:
        print("Customer has not ordered anything yet")


def customers_order(m, o):
    """Request customer for order.

    :param m: str
    :param o: str
    :return: None
    """
    cont = "y"
    while cont == "y":
        # The program asks questions to the user. The answers are then stored
        # into a list named 'order'
        pizza_name = validate_string("What type of pizza did you want "
                                     "to add? -> ", 6, 10)
        pizza_price = 0
        result = search_pizza(m, pizza_name)
        if result is not None:
            quantity_pizza = validate_integer("How many pizzas did you "
                                              "want to add? -> ", 1, 15)
            # The format which shows how the information is stored
            pizza_name = result[0]
            pizza_price = result[1]
            # This sends it back up to the order list and adds to it.
            o.append([quantity_pizza, pizza_name, pizza_price])
            print("You have added {} {} Pizzas to the list.".format(
                quantity_pizza, pizza_name))
            return None
        else:
            print("This pizza is not in the menu. Please try again")


def search_pizza(m, o):
    """Search if the order is in the menu.

    :param m: str
    :param o: str
    :return: None
    """
    for i in range(0, len(m)):
        if o == m[i][0]:
            name = m[i][0]
            price = m[i][1]
            return name, price
    return None


def change_quantity(o):
    """Change quantity of pizza in the order.

    :param o: str
    :return: None
    """
    for i in range(0, len(o)):
        # Format: Number (choices): Number of pizza which the customer
        # has ordered, Name of Pizza
        output = "{:3} : {:^13} {}".format(i+1, o[i][0], o[i][1])
        print(output)
    choice_number = validate_integer("Please enter the choice number "
                                     "to update the quantity? ", 1, 4)
    choice_number = choice_number - 1
    new_quantity = validate_integer("Please enter the new quantity: "
                                    "-> ", 1, 15)
    old_quantity = o[choice_number][1]
    o[choice_number][1] = new_quantity
    # Confirmation that the pizza quanity has changed
    output_message = "The quantity of {} pizza has now changed from "\
                     "{} to {}.".format(o[choice_number][0],
                                        old_quantity, new_quantity)
    print(output_message)


def update_order(o):
    # Another function menu in a menu
    """Another menu function for user to choose.

    :param o: str
    :return: None
    """
    # The function menu for the update function
    update_function = [
        ("R", "Review Order"),
        ("C", "Change Order Quantity"),
        ("D", "Delete Pizza"),
        ("E", "Go back to Main Menu")
    ]

    one_char_list = ["C", "D", "E"]
    c = "What type of update function did you want? "

    run = True
    while run is True:
        for i in range(0, len(update_function)):
            print("{} : {}".format(update_function[i][0],
                                   update_function[i][1]))
        choices = validate_one_char(c, one_char_list)
        if choices == "R":
            print("Review Customer's Order")
            print("-" * 23)
            review_order(o)
            print("=" * 60)
        elif choices == "C":
            print("Change Order Quantity ")
            print("-" * 23)
            change_quantity(o)
            print("=" * 60)
        elif choices == "D":
            print("Delete Order")
            print("-" * 23)
            print("You have chosen the letter D")
            print("=" * 60)
        else:
            print("--- Returning to Main Menu ---")
            print("=" * 60)
            run = False


def main():
    """Choose the main menu function.

    :return: None
    """
    print("Welcome to Marsden Pizza :)")
    # The different types of lists that is used through out the program
    functions = [
        ("M", "Pizza Menu"),
        ("R", "Review Customer's Order"),
        ("U", "Update Order"),
        ("O", "Add to Order"),
        ("C", "Cancel")
    ]

    menu = [
        ("Cheese", 9.00),
        ("Hawaiian", 10.00),
        ("Pepperoni", 7.00),
        ("Margherita", 4.00)
    ]

    one_char_list = ["M", "R", "O", "U", "C", "Q"]
    m = "Please enter menu option or enter 'C' to cancel the order -> "

    # A fake customer order list for testing
    order = []

    run = True
    while run is True:
        for i in range(0, len(functions)):
            # Format of what the function menu looks like. Numbers: Functions
            print("{} : {}".format(functions[i][0], functions[i][1]))
        option = validate_one_char(m, one_char_list)
        print("=" * 60)
        # The different options that the user can click onto
        if option == "M":
            review_menu(menu)
            print("=" * 60)
        elif option == "R":
            print("Review Customer's Order")
            print("-" * 23)
            review_order(order)
            print("=" * 60)
        elif option == "U":
            review_order(order)
            print("=" * 60)
            update_order(order)
        elif option == "O":
            review_menu(menu)
            print("=" * 60)
            customers_order(menu, order)
            print("=" * 60)
        elif option == "C":
            print("Thank You!")
            run = False
        else:
            print("Invalid Entry")
            print("=" * 60)


if __name__ == "__main__":
    main()
