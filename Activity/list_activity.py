import os

# Clear console screen
os.system('cls')

# Input list
numbers = []
occurence = 5

for i in range(occurence):
    numbers.append(int(input(f"Enter number {i + 1} value: ")))

print(numbers)

# Function to return the sum of a list
def sum_list(lst):
    return sum(lst)

# Function to return the average of a list
def average_list(lst):
    return sum(lst) / len(lst) if lst else 0

# Function to return the highest value in a list
def highest_list(lst):
    return max(lst) if lst else None

# Function to return the factorial of a number
def factorial_calculator(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Display results
print(f"Total Sum: {sum_list(numbers)}")
print(f"Average: {average_list(numbers)}")
print(f"Highest Number: {highest_list(numbers)}")

# Factorial input
num = int(input("Enter a number for factorial calculation: "))
print(f"Factorial: {factorial_calculator(num)}")

# Prime number check
num = int(input("Enter a number to check if it's prime: "))
print(f"Is {num} a prime number? {is_prime(num)}")
