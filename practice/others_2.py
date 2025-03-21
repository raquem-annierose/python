def factorial_calculator():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial: {fact}")

def divisibility_checker():
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both 3 and 5")
    else:
        print("Not divisible by both")

def smallest_number():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print("Smallest number:", min(a, b, c))

def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

def palindrome_checker():
    word = input("Enter a word: ").lower()
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

def reverse_two_digits():
    num = input("Enter a two-digit number: ")
    if len(num) == 2 and num.isdigit():
        print("Reversed:", num[::-1])
    else:
        print("Invalid input, enter a two-digit number.")

def even_digit_sum():
    num = input("Enter a number: ")
    total = sum(int(digit) for digit in num if int(digit) % 2 == 0)
    print("Sum of even digits:", total)

def character_case_checker():
    char = input("Enter a single character: ")
    if char.isupper():
        print("Uppercase letter")
    elif char.islower():
        print("Lowercase letter")
    else:
        print("Not a letter")

def prime_checker():
    num = int(input("Enter a number: "))
    if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print("Prime number")
    else:
        print("Not a prime number")

def main():
    while True:
        print("\nChoose an exercise:")
        print("1: Factorial Calculator")
        print("2: Divisibility Checker")
        print("3: Smallest Number")
        print("4: Temperature Converter")
        print("5: Palindrome Checker")
        print("6: Reverse Two Digits")
        print("7: Sum of Even Digits")
        print("8: Character Case Checker")
        print("9: Prime Number Checker")
        print("10: Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            factorial_calculator()
        elif choice == "2":
            divisibility_checker()
        elif choice == "3":
            smallest_number()
        elif choice == "4":
            temperature_converter()
        elif choice == "5":
            palindrome_checker()
        elif choice == "6":
            reverse_two_digits()
        elif choice == "7":
            even_digit_sum()
        elif choice == "8":
            character_case_checker()
        elif choice == "9":
            prime_checker()
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()