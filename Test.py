menu = [
    ("Cheese", 9.00),
    ("Hawaiian", 10.00),
    ("Pepperoni", 7.00),
    ("Margherita", 4.00)
]

order=[]

def get_string(m):
    my_string = input(m)
    return my_string

def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def customers_order(menu, order):
    cont = "y"
    while cont == "y":
        pizza_name = get_string("What type of pizza did you want to add? -> ")
        pizza_price = 0
        result = search_pizza(menu, pizza_name)
        if result is not None:
            quantity_pizza = get_integer("How many pizzas did you want to add? -> ")
            pizza_name= result[0]
            pizza_price = result[1]
            order.append([quantity_pizza, pizza_name, pizza_price])
            print("You have added {} {} Pizzas to the list.".format(quantity_pizza, pizza_name))
            return None
        else:
            print("This entry is not recognised")

def search_pizza(the_menu,item):
    #find is the pizza_name entered is in the list
    # if it is , get its row number
    for i in range(0, len(the_menu)):
        if item == the_menu[i][0]:
            name = the_menu[i][0]
            price = the_menu[i][1]
            return name, price
    return None

def review_order(l):
    print("The customer has ordered: ")
    for i in range(0, len(l)):
        output = "{:^5} {} Pizzas --- ${}".format(l[i][0], l[i][1], l[i][2])
        print(output)


customers_order(menu, order)
review_order(order)

