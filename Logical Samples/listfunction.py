# Function to get the first fruit from a list
def get_first_fruit(fruits):
    return fruits[0]  # Return the first element in the list

# Define a list of fruits and get the first fruit
my_fruits = ['Apple', 'Banana', 'Grapes']
first = get_first_fruit(my_fruits)
print("First fruit is:", first)  # Output: First fruit is: Apple

# Function to print all fruits in a list
def print_fruits(fruit_list):
    for fruit in fruit_list:  # Iterate through the list
        print(fruit)  # Print each fruit

# Call the function with a list of fruits
print_fruits(['Cherry', 'Apple', 'Orange'])
# Output:
# Cherry
# Apple
# Orange

# Function to count the total number of fruits in a list
def count_fruits(fruit_list):
    return len(fruit_list)  # Return the length of the list

# Define a list of fruits and count the total
my_list = ['Cherry', 'Apple', 'Orange']
total = count_fruits(my_list)
print("Total fruits:", total)  # Output: Total fruits: 3

# Function to greet a person by name
def greet(name):
    if not name:  # Check if the name is empty or None
        print("Name is missing.")  # Print a message if the name is missing
        return  # Exit the function
    print(f"Hello, {name}!")  # Print a greeting message

# Call the greet function with a name
greet("Liam")  # Output: Hello, Liam!
# Call the greet function without a name
greet("")  # Output: Name is missing.