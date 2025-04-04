# 🔸 Challenge 7: Capitalize All
# This function capitalizes all the words passed in.
def capitalize_all(*words):
    return [word.capitalize() for word in words]

print("Capitalized words:", capitalize_all("hello", "world", "python", "rocks"))


# 🔸 Challenge 7: Capitalize All
# This function capitalizes all the words passed in.
def capitalize_all(*words):
    return [word.capitalize() for word in words]

print("Capitalized words:", capitalize_all("hello", "world", "python", "rocks"))


# 🔸 Challenge 9: Multiply by Factor
# This function multiplies all numbers by a given factor.
def multiply_by_factor(factor, *numbers):
    return [factor * num for num in numbers]

print("Multiplied by 3:", multiply_by_factor(3, 1, 2, 3, 4))


# 🧪 Coding Challenge 7: Filter Strings
# This function returns only the values that are strings.
def filter_strings(**kwargs):
    return [value for value in kwargs.values() if isinstance(value, str)]

print("Filtered strings:", filter_strings(a=1, b="banana", c="apple", d=5.5, e="grape"))


# 🧪 Coding Challenge 8: Word Lengths
# This function returns a dictionary of each word and its length.
def word_lengths(*words):
    return {word: len(word) for word in words}

print("Word lengths:", word_lengths("hello", "world", "python", "amazing"))

# 🧪 Coding Challenge 9: Check All Even
# This function checks if all given numbers are even.
def all_even(*numbers):
    return all(num % 2 == 0 for num in numbers)

print("Are all even?", all_even(2, 4, 6, 8))
print("Are all even?", all_even(2, 3, 6))


# 🧪 Coding Challenge 10: Build a Sentence
# This function takes any number of words and joins them into a sentence.
def build_sentence(*words):
    return ' '.join(words).capitalize() + '.'

print("Sentence:", build_sentence("coding", "in", "python", "is", "fun"))


