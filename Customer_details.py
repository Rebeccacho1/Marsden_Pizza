"""Fruitbowl management program"""
from Validations import validate_one_char, validate_string, validate_integer

def customer_details():
    ordering = validate_string("How are you going to receive your order?/n - Deliver or Pick Up ", 7, 7).upper


if __name__ == "__main__":
    customer_details()
