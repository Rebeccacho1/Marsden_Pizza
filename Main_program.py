"""Fruitbowl management program"""
from Validations import validate_one_char, validate_string, validate_integer

# A function when the user wants to see the menu and also helps format
def review_menu(m):
    print("Pizza Menu")
    print("-" * 10)
    for i in range(0, len(m)):
#:.2f - changed it so it's two decimal places
        output = "{:^15} --- ${:.2f}".format(m[i][0], m[i][1])
        print(output)

def review_order(o):
    if len(o) != 0:
        print("The customer has ordered: ")
        for i in range(0, len(o)):
            output = "{:^3} {:^13} Pizzas --- ${}".format(o[i][0], o[i][1], o[i][2])
            print(output)
    else:
        print("Customer has not ordered anything yet")

def customers_order(m, o):
    run = True
    while run is True:
        pizza_name = validate_string("What type of pizza did you want to add? -> ", 6, 10).upper()
        pizza_price = 0
        result = search_pizza(m, pizza_name)
        if result is not None:
            quantity_pizza = validate_integer("How many pizzas did you want to add? -> ", 1, 15)
            pizza_name = result[0]
            pizza_price = result[1]
            o.append([quantity_pizza, pizza_name, pizza_price])
            print("You have added {} {} Pizzas to the list.".format(quantity_pizza, pizza_name))
            incorrect_choice = True
            while incorrect_choice is True:
                another_pizza = validate_string("Would you like to add another pizza? (Yes/No) ", 2, 3).upper()
                if another_pizza == "YES":
                    incorrect_choice = False
                elif another_pizza == "NO":
                    return None
                else:
                    print("Your answer is incorrect please try again")
                    continue
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
    # Structure - [quantity_pizza, pizza_name, pizza_price]
    if len(o) != 0:
        for i in range (0, len(o)):
            output = "{:2} : {:^4} {} Pizzas".format(i+1, o[i][0], o[i][1])
            print(output)
        choice_number =  validate_integer("Please enter the choice number to update the quantity? ", 1, 50)
        # the choice number is up to 1 to 4. - you can change it anytime
        choice_number = choice_number - 1
        new_quantity = validate_integer("Please enter the new quantity: -> ", 1, 15)
        old_quantity = o[choice_number][0]
        o[choice_number][0] = new_quantity
        output_message = "The quantity of {} pizza has now changed from {} to {}.".format(o[choice_number][1], old_quantity, new_quantity)
        print(output_message)
    else:
        print("Customer has not ordered anything yet")

def delete_pizza(o):
    run = True
    while run is True:
        if len(o) != 0:
            for i in range (0, len(o)):
                output = "{:2} : {:^4} {} Pizzas".format(i+1, o[i][0], o[i][1])
                print(output)
            delete_option = validate_string("Did you want to restart order or remove a pizza?\n"
                                            "- Please type 'RESTART' or 'REMOVE' --> ", 5, 8).upper()
            if delete_option == "RESTART":
                o.clear()
                print("=" * 60)
                print("--- Order is being erased ---")
                print("=" * 60)
                review_order(o)
            elif delete_option == "REMOVE":
                get_deletions = True
                while get_deletions:
                    chosen_number = validate_integer("Please enter the choice number to delete the pizza? ", 1, len(o))
                    chosen_number = chosen_number - 1
                    print("The {} pizza is being removed".format(o[chosen_number][1]))
                    o.pop(chosen_number)
                    repeat_delete = True
                    while repeat_delete is True:
                        another_delete = validate_string("Would you like to delete another pizza? (Yes/No) ", 2, 3).upper()
                        if another_delete == "YES":
                            repeat_delete = False
                        elif another_delete == "NO":
                            return None
                        else:
                            print("Your answer is incorrect. Please try again")
            else:
                print("Your answer is incorrect please try again")
        else:
            return

def update_order(o):
    update_function = [
        ("R", "Review Order"),
        ("C", "Change Order Quantity"),
        ("D", "Delete Pizza"),
        ("E", "Go back to Main Menu")
    ]

    one_char_list = ["R", "C", "D", "E"]
    c = "What type of update function did you want? "

    run = True
    while run is True:
        for i in range(0, len(update_function)):
            print("{} : {}".format(update_function[i][0], update_function[i][1]))
        choices = validate_one_char(c, one_char_list)
        print("=" * 60)
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
            delete_pizza(o)
            print("=" * 60)
        else:
            print("--- Returning to Main Menu ---")
            print("=" * 60)
            run = False

def customer_details(c):
    user_name = validate_string("What is the name for your order -> ", 3, 10)
    phone_number = validate_string("Phone number - ", 5, 20)
    run = True
    while run is True:
        receive_order = validate_string("How are you going to receive your order?\n"
                                        "- Deliver or Pick Up --> ", 6, 7).upper()
        print("=" * 60)
        if receive_order == "DELIVER":
            print("$3 is going to be charged for delivery")
            street_number = validate_string("Please enter your street number - ", 1, 4)
            street_name = validate_string("Street Name - ", 2, 100)
            suburb = validate_string("Suburb - ", 2, 100)
            postcode = validate_string("Postcode - ", 2, 100)
            print("=" * 60)
            c.append([user_name, phone_number, street_number, street_name, suburb, postcode])
            print("--- Please check the following details with the customer ---")
            print("             Order for: {}".format(c[0][0]))
            print("          Phone Number: {}".format(c[0][1]))
            print("Street Number & Number: {} {},".format(c[0][2], c[0][3]))
            print("    Suburb & Postcode : {}, {}".format(c[0][4], c[0][5]))
            print("=" * 60)
            return street_number, street_name, suburb, postcode
        elif receive_order in ["PICK UP" ,"PICKUP"]:
            c.append([user_name, phone_number])
            print("--- Please check the following details with the customer ---")
            print("   Order for: {}".format(c[0][0]))
            print("Phone Number: {}".format(c[0][1]))
            print("=" * 60)
            return
        else:
            print("Please try again. I didn't get that")
        continue

def main():
    print("Welcome to Marsden Pizza :)")
    customer_list = []
    customer_details(customer_list)
    functions = [
        ("M", "Pizza Menu"),
        ("R", "Review Customer's Order"),
        ("U", "Update Order"),
        ("O", "Add to Order"),
        ("C", "Cancel")
    ]

    menu = [
        ("CHEESE", 9.0),
        ("HAWAIIAN", 10.0),
        ("PEPPERONI", 7.0),
        ("MARGHERITA", 4.0),
    ]

    one_char_list = ["M", "R", "O", "U", "C", "Q"]
    m = "Please enter menu option or enter 'C' to cancel the order -> "

    order = []
    order_test = [
        [3,"Cheese", 9.00],
        [4, "Pepperoni", 7.00],
        [1, "Margherita", 4.00]
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
