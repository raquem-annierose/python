fruits = {}
user_input = input("enter a fruit").lower
while True:
    dict_fruits = input("Enter a fruit: ")

    if dict_fruits in dict:
        dict[dict_fruits] += 1
    elif dict_fruits.lower() != 'exit':
        dict[dict_fruits] = 1
    else:
        break

print(dict)