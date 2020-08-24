



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
            output = "{:^5} {} Pizzas --- ${}".format(o[i][0], o[i][1], o[i][2])
            print(output)
    else:
        print("Customer has not ordered anything yet")

def customers_order(m, o):
    cont = "y"
    while cont == "y":
        pizza_name = get_string("What type of pizza did you want to add? -> ")
        pizza_price = 0
        result = search_pizza(m, pizza_name)
        if result is not None:
            quantity_pizza = get_integer("How many pizzas did you want to add? -> ")
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

def main():
    print("Main Menu")
    functions = [
        ("1", "Pizza Menu"),
        ("2", "Review Customer's Order"),
        ("3", "Order"),
        ("Q", "Quit")
    ]

    menu = [
        ("Cheese", 9.00),
        ("Hawaiian", 10.00),
        ("Pepperoni", 7.00),
        ("Margherita", 4.00)
    ]

    order = []
    run = True
    while run is True:
        for i in range(0, len(functions)):
            print("{} : {}".format(functions[i][0], functions[i][1]))
        option = get_string("Choose the options by number or enter 'C' to cancel the order -> ")
        print("=" * 60)
        if option == "1":
            review_menu(menu)
            print("=" * 60)
        elif option == "2":
            print("Review Customer's Order")
            print("-" * 23)
            review_order(order)
            print("=" * 60)
        elif option == "3":
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
