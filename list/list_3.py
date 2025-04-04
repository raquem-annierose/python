number = int(input("Enter a number (0 to 5): "))  # Prompt user with valid range

food = ["Chocolate", "Burgers", "Fries", "Soda", "Chicken"]

food.insert(5, "Pizza")  # Add "Pizza" at index 5

print(food)  # Print the entire list

# Check if the input number is within the valid range
if 0 <= number < len(food):
    print(food[number])  # Print the food item at the given index
else:
    print("Invalid number. Please enter a number between 0 and", len(food) - 1)