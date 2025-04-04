# 🔸 Challenge 4: Reverse All Words
# This function takes any number of words and returns a list of those words reversed.
def reverse_words(*words):
    return [word[::-1] for word in words]

print("Reversed words:", reverse_words("hello", "world", "python"))


# 🔸 Challenge 5: Greet People
# This function greets each person passed as an argument.
def greet_people(*names):
    for name in names:
        print(f"Hello, {name}!")

print("Greeting people:")
greet_people("Alice", "Bob", "Charlie")


# 🔸 Challenge 6: Favorite Things
# This function prints out someone's favorite things using keyword arguments.
def favorite_things(**kwargs):
    for thing, value in kwargs.items():
        print(f"My favorite {thing} is {value}.")

print("Favorite Things:")
favorite_things(food="pizza", color="blue", sport="basketball", animal="dog")


# 🧪 Coding Challenge 4: Average of Numbers
# This function returns the average of all numbers provided.
def average(*nums):
    return sum(nums) / len(nums) if nums else 0

print("Average:", average(10, 20, 30, 40))


# 🧪 Coding Challenge 5: Keyword Stats
# This function prints the number of keyword arguments and lists their keys.
def keyword_stats(**kwargs):
    print("Total keywords:", len(kwargs))
    print("Keys:", list(kwargs.keys()))

print("Keyword Stats:")
keyword_stats(name="Liam", age=25, country="Canada", hobby="skiing")


# 🧪 Coding Challenge 6: Is Palindrome?
# This function checks if each word is a palindrome and returns results.
def check_palindromes(*words):
    return {word: word == word[::-1] for word in words}

print("Palindrome check:", check_palindromes("level", "radar", "hello", "world"))


