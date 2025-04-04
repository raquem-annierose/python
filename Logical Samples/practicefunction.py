#without return

def greet():
    print("Hello, Annie!")

greet()

#with input
def greet(msg):
    print(f"Greetings: {msg}")

greet("Hello World!")

#Function with return
def add(a, b):
    result = a + b
    return result


sum = add(5, 3)
print(sum)  # Output: 8


#Function with parameters
def greet(message, sender, receiver):
    print(f"To: {receiver} !")
    print(f"Message: {message}")
    print(f"From: {sender}")

greet("Welcome to the team!", "Steven", "John")

#Function with return
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = celsius_to_fahrenheit(36)
print(celsius)

