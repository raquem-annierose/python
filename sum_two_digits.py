num = int(input("Enter a two-digit number: "))

digit1 = num // 10  # Extracts the tens place
digit2 = num % 10   # Extracts the ones place

print(f"The sum of the digits is {digit1 + digit2}.")
