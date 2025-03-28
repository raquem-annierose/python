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




