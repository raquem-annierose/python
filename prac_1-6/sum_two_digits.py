num = int(input("Enter a two-digit number: "))

if 10 <= num >= 99:
    digit_1 = num // 10
    digit_2 = num % 10   
    print(f"The sum of the digits is {digit_1 + digit_2}.")
else:
    print("Please enter 2 digit")


