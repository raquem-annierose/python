num = int(input("Enter a number: "))

if num == 0:
    print("The number is zero.")
elif num % 2 == 0:
    print("The number is even.")
elif num % 2 != 0:
    print("The number is odd.")
else:
    print("Invalid input.")
