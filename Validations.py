def validate_one_char(m, char_list):
    while True:
        user_input = input(m)
        user_input = user_input.upper().strip()[0]
        if user_input in char_list:
            return user_input
        else:
            print("Please try again, that is not a choice from the menu. ")

def validate_string(m, min, max):
    while True:
        get_string = input(m)
        if len(get_string) < min:
            print("That's too little characters, please check if you have typed in the right words")
        elif len(get_string) > max:
            print("There's too many characters, please check if you have typed in the right words")
        else:
            return get_string

def validate_integer(m, min, max):
    while True:
        try:
            get_integer = int(input(m))
        except ValueError:
            print("Sorry, that entry is incorrect. Please try again")
            continue
        if get_integer < min:
            print("The number you have entered is too small. Please try again")
            continue
        elif get_integer > max:
            print("The number you have entered is too large. Please try again")
            continue
        else:
            return get_integer



