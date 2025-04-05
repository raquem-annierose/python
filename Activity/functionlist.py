import os
import math

# Clear console screen
os.system('cls')

# Input list
numbers = []
occurence = 5

for i in range(occurence):
    numbers.append(int(input(f"Enter number {i + 1} value: ")))

print(numbers)


def smallest_list(lst):
    return min(lst) 

print(f"Minimum Number: {smallest_list(numbers)}")

def reverse_string(text):
    return text[::-1]  # Slicing method to reverse

text = "hello"
print(reverse_string(text))  # Output: "olleh"

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)  # Counts vowels

sentence = "Programming is fun"
print(count_vowels(sentence))  # Output: 6

def is_even(number):
    return number % 2 == 0  # True if even, False if odd

number = 7
print(is_even(number))  # Output: False

def is_odd(number):
    return number % 2 != 0  # True if even, False if odd

number = 7
print(is_odd(number))  # Output: False

def second_largest(lst):
    unique_numbers = list(set(lst))  # Remove duplicates
    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1] if len(unique_numbers) > 1 else None  # Second largest

numbers = [12, 45, 2, 8, 30]
print(second_largest(numbers))  # Output: 30

import math

def gcd(num1, num2):
    return math.gcd(num1, num2)  # Uses built-in GCD function

num1, num2 = 36, 60
print(gcd(num1, num2))  # Output: 12


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
print(f"Factorial of {number}: {factorial(number)}")  # Output: 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
print(f"Factorial of {number}: {factorial(number)}")  # Output: 120

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

number = 29
print(f"Is {number} a prime number? {is_prime(number)}")  # Output: True

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

number = 12345
print(f"Sum of digits of {number}: {sum_of_digits(number)}")  # Output: 15

def sort_list(lst):
    return sorted(lst)

numbers = [12, 45, 2, 8, 30]
print(f"Sorted List: {sort_list(numbers)}")  # Output: [2, 8, 12, 30, 45]



def test_functions():
    # Test smallest_list
    test_numbers = [12, 45, 2, 8, 30]
    print(f"Test Numbers: {test_numbers}")
    print(f"Minimum Number: {smallest_list(test_numbers)}")  # Output: 2

    # Test reverse_string
    test_text = "hello"
    print(f"Original Text: {test_text}")
    print(f"Reversed Text: {reverse_string(test_text)}")  # Output: "olleh"

    # Test count_vowels
    test_sentence = "Programming is fun"
    print(f"Test Sentence: {test_sentence}")
    print(f"Vowel Count: {count_vowels(test_sentence)}")  # Output: 6

    # Test is_even
    test_number = 7
    print(f"Test Number: {test_number}")
    print(f"Is Even: {is_even(test_number)}")  # Output: False

    # Test second_largest
    print(f"Second Largest Number: {second_largest(test_numbers)}")  # Output: 30

    # Test gcd
    test_num1, test_num2 = 36, 60
    print(f"Numbers for GCD: {test_num1}, {test_num2}")
    print(f"GCD: {gcd(test_num1, test_num2)}")  # Output: 12

# Call the test function
test_functions()