"""Fruitbowl management program"""
from Validations import validate_one_char, validate_string, validate_integer

def customer_details(c_l):
    user_name = validate_string("What is your name for the order -> ", 3, 10)
    phone_number = validate_string("Phone number - ", 5, 20)
    run = True
    while run is True:
        receive_order = validate_string("How are you going to receive your order?\n"
                                        "- Deliver or Pick Up --> ", 7, 7).upper()
        print("-" * 60)
        if receive_order == "DELIVER":
            print("$3 is going to be charged for delivery")
            street_number = validate_string("Please enter your street number - ", 1, 4)
            street_name = validate_string("Street Name - ", 2, 100)
            suburb = validate_string("Suburb - ", 2, 100)
            postcode = validate_string("Postcode - ", 2, 100)
            c_l.append([user_name, phone_number, street_number, street_name, suburb, postcode])
            return street_number, street_name, suburb, postcode
        elif receive_order == "PICK UP":
            c_l.append([user_name, phone_number])
            return
        else:
            print("Please try again. I didn't get that")
        continue

def checking_details(customer_list):
    customer_details(customer_list)
    print("=" * 60)
    print("-" * 60)
    print("--- Please check the following details with the customer ---")
    print("-" * 60)
    print("Order for : {}".format(user_name))




if __name__ == "__main__":
    checking_details()
