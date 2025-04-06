# Define a dictionary representing a person with keys: name, age, and hobby
person = {
    "name": "Liam",
    "age": 21,
    "hobby": "photography"
}

# Access and print the value associated with the "name" key
print(person["name"])  # Output: Liam

# Print the entire dictionary
print(person)  # Output: {'name': 'Liam', 'age': 21, 'hobby': 'photography'}

#printloop
for key, value in person.items():
    print(f"{key} = {value}")


# Check if the key "hobby" exists in the dictionary
if "hobby" in person:
    print("Found hobby!")  # Output: Found hobby!

# Add a new key-value pair to the dictionary
person["country"] = "Philippines"
print(person)  # Output: {'name': 'Liam', 'age': 21, 'hobby': 'photography', 'country': 'Philippines'}

# Iterate through the dictionary and print each key-value pair
for key in person:
    print(key, "=", person[key])
    # Output:
    # name = Liam
    # age = 21
    # hobby = photography
    # country = Philippines

# Define a nested dictionary representing a user profile
profile = {
    "username": "Liam123",
    "contacts": {
        "email": "Liame@mail.com",
        "phone": "123456789"
    },
    "likes": ["coding", "editing", "vlogging"]
}

# Access and print the email address from the nested dictionary
print("")
print(profile["contacts"]["email"])  # Output: Liame@mail.com



# Function to calculate the sum of arbitrary positional arguments (*args)
def add_all(*args):
    total = sum(args)  # Calculate the sum of all arguments
    print("Total:", total)

# Call the function with different numbers of arguments
add_all(1, 2, 3)          # Output: Total: 6




# Function to display arbitrary keyword arguments (**kwargs)
def display_info(**kwargs):
    for key, value in kwargs.items():  # Iterate through the key-value pairs
        print(f"{key} = {value}")

# Call the function with keyword arguments
display_info(name="Liam", hobby="editing", age=21)
# Output:
# name = Liam
# hobby = editing
# age = 21

# Demonstrate different ways of printing strings
print("AB")  # Output: AB
print("A" + "B")  # Output: AB (string concatenation)
print("A", end="B")  # Output: AB (no newline, "B" is appended directly)
print("\nA", end="\nB")  # Output: A (on a new line), B (on another new line)