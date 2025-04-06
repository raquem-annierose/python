def highest_value(dict):
    max_value = max(dict.values())
    for key, value in dict.items():
       if value == max_value:
          return key
       
my_dict = {
           "John": "80",
           "Alice": "92", 
           "Bob": "85", 
           "Charlie": "92"
          }
print(highest_value(my_dict))

print(highest_value({
                    "John": "80", 
                    "Alice": "92", 
                    "Bob": "85", 
                    "Charlie": "92"
                   }))

def invert_dict(elements):
  inverted_dict = {}
  for key, value in elements.items():
    inverted_dict[value] = key
  return inverted_dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dict(my_dict)
print(inverted_dict) 

def dictionary_to_list_tuple (dict):
    return list(dict.items())

original_dict = {
                "a": "1", 
                "b": "2",
                "c": "3"
                }
print(dictionary_to_list_tuple(original_dict))