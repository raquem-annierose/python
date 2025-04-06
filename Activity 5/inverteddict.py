# def get_key_with_max_value(elements):
#   max_value = max(elements.values())
#   for key, value in elements.items():
#     if value == max_value:
#       return key

# my_dict = {'John': 80, 'Alice': 92, 'Bob': 85, 'Charlie': 92}
# result = get_key_with_max_value(my_dict)
# print(result)  
def first_key_with_highest_value(dict):
    highest_value = max(dict.values())  # Find the highest value
    for key, value in dict.items():  # Iterate through key-value pairs
        if value == highest_value:  # Check if the value matches the highest value
            return key  # Return the first matching key

scores = {'John': 82, 'Alice': 92, 'Bob': 85, 'Charlie': 92}
print(first_key_with_highest_value(scores))  # Output: 'Alice'

def invert_dict(elements):
 
  inverted_dict = {}
  for key, value in elements.items():
    inverted_dict[value] = key
  return inverted_dict

my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
inverted_dict = invert_dict(my_dict)
print(inverted_dict)  