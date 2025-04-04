# Function to find the first key with the highest value in a dictionary
def first_key_with_highest_value(dict):
    highest_value = max(dict.values())  # Find the highest value
    for key, value in dict.items():  # Iterate through key-value pairs
        if value == highest_value:  # Check if the value matches the highest value
            return key  # Return the first matching key

scores = {'John': 82, 'Alice': 92, 'Bob': 85, 'Charlie': 92}
print(first_key_with_highest_value(scores))  # Output: 'Alice'


# Function to invert a dictionary (swap keys and values)
def invert_dictionary(input_dict):
    return {v: k for k, v in input_dict.items()}  # Swap keys and values

original_dict = {'a': 1, 'b': 2, 'c': 3}
print(invert_dictionary(original_dict))  # Output: {1: 'a', 2: 'b', 3: 'c'}


# Function to convert a dictionary into a list of tuples
def dict_to_list_of_tuples(dict):
    return list(dict.items())  # Convert key-value pairs to a list of tuples

original_dict = {'a': 1, 'b': 2, 'c': 3}
print(dict_to_list_of_tuples(original_dict))  # Output: [('a', 1), ('b', 2), ('c', 3)]