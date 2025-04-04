# def get_key_with_max_value(elements):
#   max_value = max(elements.values())
#   for key, value in elements.items():
#     if value == max_value:
#       return key

# my_dict = {'John': 80, 'Alice': 92, 'Bob': 85, 'Charlie': 92}
# result = get_key_with_max_value(my_dict)
# print(result)  

def invert_dict(elements):
 
  inverted_dict = {}
  for key, value in elements.items():
    inverted_dict[value] = key
  return inverted_dict

my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
inverted_dict = invert_dict(my_dict)
print(inverted_dict)  