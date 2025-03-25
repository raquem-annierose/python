def get_sum_of_digits(value):
    if not value.isdigit():
        print("Not a number.")
        return 0
    tens_digit = int(value[0])
    ones_digit = int(value[1])
    return tens_digit + ones_digit

user_input = input("Enter a 2 digit number: ")
print(get_sum_of_digits(user_input))

