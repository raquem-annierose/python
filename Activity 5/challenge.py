# 🔸 Challenge 1: Return the longest word
# This function takes any number of words and returns the one with the longest length.
def longest_word(*words):
    return max(words, key=len)

print("Longest word:", longest_word("apple", "banana", "cherry", "dragonfruit"))


# 🔸 Challenge 2: Describe a person using **kwargs
# This function accepts any number of keyword arguments and prints them as key-value pairs.
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("Person Description:")
describe_person(name="Alice", age=30, job="Engineer", hobby="Painting")

# 🔸 Challenge 3: Custom Calculator
# This function accepts an operation ("add" or "multiply") and any number of numeric values.
# It performs the selected operation on all the numbers.
def custom_calc(operation, *numbers):
    if operation == "add":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        return "Unsupported operation"
    
print("Sum:", custom_calc("add", 1, 2, 3, 4))
print("Product:", custom_calc("multiply", 2, 3, 4))
print("Unknown Operation:", custom_calc("divide", 2, 3))


# 🧪 Coding Challenge 1: Sum of Squares
# This function takes any number of arguments and returns the sum of their squares.
def sum_squares(*args):
    return sum(x**2 for x in args)

print("Sum of squares:", sum_squares(1, 2, 3, 4))


# 🧪 Coding Challenge 2: Only Even Keywords
# This function accepts any number of keyword arguments and prints values that are even numbers.
def only_even_values(**kwargs):
    for value in kwargs.values():
        if isinstance(value, int) and value % 2 == 0:
            print(value)

print("Even values only:")
only_even_values(a=1, b=2, c=3, d=4, e="hello", f=6)


# 🧪 Coding Challenge 3: Count Words
# This function takes a string and returns the number of words in it.
def count_words(text):
    return len(text.split())

sentence = "This is a sample sentence with seven words."
print("Word count:", count_words(sentence))