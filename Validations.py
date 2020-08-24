def validate_string(m, min, max):
    while True:
        get_string = input(m)
        if len(get_string) < min:
            print("There are no pizzas with the length of the ")
        elif len(get_string) > max:
            print("There's too many words")
        else:
            return get_string

if __name__ == "__main__":
    test = validate_string("Please enter your number: -> ", 0, 10)
    #test = get_validated_integer("Please enter your number: -> ", 0, 5)
    print(test)