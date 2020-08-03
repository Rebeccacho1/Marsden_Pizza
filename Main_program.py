def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def review_menu(m):
    for i in range(0, len(m)):
        output = "{:^15} --- {}".format(m[i][0], m[i][1])
        print(output)

def review_order(m):
    for i in range(0, len(m)):
        print("The customer has ordered: ")
        output = "{:^5} {} Pizzas".format(m[i][0], m[i][1])
        print(output)

def customers_order(m):
    cont = "x"
    while cont == "x":
        pizza_name = get_string("What type of pizza did you want to add? -> " )
        quantity_pizza = get_integer("How many pizzas did you want to add? -> ")
        order = [quantity_pizza, pizza_name]
        m.append(order)
        print("You have added {} {} Pizzas to the list.".format(quantity_pizza, pizza_name))
        return None

def main():
    print("Main Menu")
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
            print("{} : {}".format(functions[i][0], functions[i][1]))
        option = get_string("Choose the options by number or enter 'Q' to quit -> ")
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
