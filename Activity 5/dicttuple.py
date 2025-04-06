
def dict_to_list_of_tuples(dict):
    return list(dict.items())

original_dict = {'d': 4,
                 'a': 1,
                 'b': 2, 
                 'c': 3,
                 ("apples", "oranges" ): 5}
print(dict_to_list_of_tuples(original_dict)) 
