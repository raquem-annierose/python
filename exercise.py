print("1. Check Equality")
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if num_1 == num_2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

print("\n2. Odd, Even, or Zero")
num = int(input("Enter a number: "))

if num == 0:
    print("The number is zero.")
elif num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("\n3. Highest Number")
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if num_1 >= num_2 and num_1 >= num_3:
    highest = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    highest = num_2
else:
    highest = num_3

print(f"The highest number is {highest}.")

print("\n4. Coordinate Quadrantr")
x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("The point is in Quadrant I.")
elif x < 0 and y > 0:
    print("The point is in Quadrant II.")
elif x < 0 and y < 0:
    print("The point is in Quadrant III.")
elif x > 0 and y < 0:
    print("The point is in Quadrant IV.")
elif x == 0 and y != 0:
    print("The point is on the Y-axis.")
elif y == 0 and x != 0:
    print("The point is on the X-axis.")
else:
    print("The point is at the origin.")


print("\n5. Consonant or Vowel")
char = input("Enter a character: ").lower()

if char in 'aeiou':
    print("The character is a vowel.")
elif char.isalpha():
    print("The character is a consonant.")
else:
    print("Invalid input. Please enter a letter.")

print("\n6. Sum Two Digits")
num = int(input("Enter a two-digit number: "))

digit1 = num // 10
digit2 = num % 10   

print(f"The sum of the digits is {digit1 + digit2}.")
print("\nExiting program...")


