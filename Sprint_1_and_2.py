"""Collect order for a Pizza Company."""


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
    for i in range(0, len(m)):
        # Helps format all of the pizzas and prices so it's all on the same
        # line and easier for the user to understand. Name of Pizza: Prices
        output = "{:^15} --- {}".format(m[i][0], m[i][1])
        print(output)


def review_order(m):
    """Review the pizza order.

    :param m: str
    :return: None
    """
    for i in range(0, len(m)):
        print("The customer has ordered: ")
        # Formats number and the name of the pizza in this output. Number, Name
        # of the pizza
        output = "{:^5} {} Pizzas".format(m[i][0], m[i][1])
        print(output)


def customers_order(m):
    """Request customer for order.

    :param m: str
    :return: None
    """
    cont = "x"
    while cont == "x":
        # The program asks questions to the user. The answers are then stored
        # into a list named 'order'
        pizza_name = get_string("What type of pizza did you want to add? -> ")
        quantity_pizza = get_integer("How many pizzas did you want "
                                     "to add? -> ")
        # The format which shows how the information is stored
        order = [quantity_pizza, pizza_name]
        # This sends it back up to the order list and adds to it.
        m.append(order)
        print("You have added {} {} Pizzas to the list.".format(quantity_pizza,
                                                                pizza_name))
        return None


def main():
    """Choose the main menu function.

    :return: None
    """
    print("Main Menu")
    # The different types of lists that is used through out the program
    functions = [
        ("1", "Pizza Menu"),
        ("2", "Review Customer's Order"),
        ("3", "Order"),
        ("Q", "Quit")
    ]
    menu = [
        ("Classic Cheese", "$9.00"),
        ("Hawaiian", "10.00")
    ]
    order = []
    run = True
    while run is True:
        for i in range(0, len(functions)):
            # Format of what the function menu looks like. Numbers: Functions
            print("{} : {}".format(functions[i][0], functions[i][1]))
        option = get_string("Choose the options by number or enter 'Q' "
                            "to quit -> ")
        print("-" * 60)
        if option == "1":
            print("Pizza Menu")
            review_menu(menu)
            print("-" * 60)
        elif option == "2":
            print("Review Customer's Order")
            review_order(order)
            print("-" * 60)
        elif option == "3":
            print("Order Pizza")
            customers_order(order)
            print("-" * 60)
        elif option == "Q":
            print("Thank You!")
            run = False
        else:
            print("Invalid Entry")


if __name__ == "__main__":
    main()
