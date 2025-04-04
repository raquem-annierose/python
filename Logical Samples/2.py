def factorial_calculator(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return f"Factorial: {fact}"

def divisibility_checker(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Divisible by both 3 and 5"
    else:
        return "Not divisible by both"

def smallest_number(a, b, c):
    return f"Smallest number: {min(a, b, c)}"

def temperature_converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"Temperature in Fahrenheit: {fahrenheit:.2f}°F"

def palindrome_checker(word):
    word = word.lower()
    if word == word[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"

def reverse_two_digits(num):
    if len(num) == 2 and num.isdigit():
        return f"Reversed: {num[::-1]}"
    else:
        return "Invalid input, enter a two-digit number."

def even_digit_sum(num):
    total = sum(int(digit) for digit in num if int(digit) % 2 == 0)
    return f"Sum of even digits: {total}"

def character_case_checker(char):
    if char.isupper():
        return "Uppercase letter"
    elif char.islower():
        return "Lowercase letter"
    else:
        return "Not a letter"

def prime_checker(num):
    if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        return "Prime number"
    else:
        return "Not a prime number"

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
            num = int(input("Enter a number: "))
            result = factorial_calculator(num)
            print(result)
        elif choice == "2":
            num = int(input("Enter a number: "))
            result = divisibility_checker(num)
            print(result)
        elif choice == "3":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            c = int(input("Enter third number: "))
            result = smallest_number(a, b, c)
            print(result)
        elif choice == "4":
            celsius = float(input("Enter temperature in Celsius: "))
            result = temperature_converter(celsius)
            print(result)
        elif choice == "5":
            word = input("Enter a word: ")
            result = palindrome_checker(word)
            print(result)
        elif choice == "6":
            num = input("Enter a two-digit number: ")
            result = reverse_two_digits(num)
            print(result)
        elif choice == "7":
            num = input("Enter a number: ")
            result = even_digit_sum(num)
            print(result)
        elif choice == "8":
            char = input("Enter a single character: ")
            result = character_case_checker(char)
            print(result)
        elif choice == "9":
            num = int(input("Enter a number: "))
            result = prime_checker(num)
            print(result)
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
