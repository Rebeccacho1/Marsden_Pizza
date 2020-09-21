"""Fruitbowl management program"""
from Validations import validate_one_char, validate_string, validate_integer

def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def review_menu(m):
    print("Pizza Menu")
    print("-" * 10)
    for i in range(0, len(m)):
        output = "{:^15} --- ${}".format(m[i][0], m[i][1])
        print(output)

def review_order(o):
    if len(o) != 0:
        print("The customer has ordered: ")
        for i in range(0, len(o)):
            output = "{:12} {} Pizzas --- ${}".format(o[i][0], o[i][1], o[i][2])
            print(output)
    else:
        print("Customer has not ordered anything yet")

def customers_order(m, o):
    cont = "y"
    while cont == "y":
        pizza_name = validate_string("What type of pizza did you want to add? -> ", 6, 10)
        pizza_price = 0
        result = search_pizza(m, pizza_name)
        if result is not None:
            quantity_pizza = validate_integer("How many pizzas did you want to add? -> ", 1, 15)
            pizza_name = result[0]
            pizza_price = result[1]
            o.append([quantity_pizza, pizza_name, pizza_price])
            print("You have added {} {} Pizzas to the list.".format(quantity_pizza, pizza_name))
            return None
        else:
            print("This pizza is not in the menu. Please try again")

def search_pizza(m,o):
    for i in range(0, len(m)):
        if o == m[i][0]:
            name = m[i][0]
            price = m[i][1]
            return name, price
    return None

def change_quantity(o):
    for i in range (0, len(o)):
        output = "{:3} : {:^13} {}".format(i+1, o[i][0], o[i][1])
        print(output)
    choice_number =  validate_integer("Please enter the choice number to update the quantity? ", 1, 4)
    choice_number = choice_number - 1
    new_quantity = validate_integer("Please enter the new quantity: -> ", 1, 15)
    old_quantity = o[choice_number][1]
    o[choice_number][1] = new_quantity
    output_message = "The quantity of {} pizza has now changed from {} to {}.".format(o[choice_number][0], old_quantity, new_quantity)
    print(output_message)

def update_order(o):
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
            print("{} : {}".format(update_function[i][0], update_function[i][1]))
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
    print("Welcome to Marsden Pizza :)")
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

    order = []
    order_test = [
        ["Cheese", 3, 9.00],
        ["Pepperoni", 4, 7.00],
        ["Margherita", 1, 4.00]
    ]
    order=order_test

    run = True
    while run is True:
        for i in range(0, len(functions)):
            print("{} : {}".format(functions[i][0], functions[i][1]))
        option = validate_one_char(m, one_char_list)
        print("=" * 60)
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
