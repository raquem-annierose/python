def greet(msg):
    print(f"Greetings: {msg}")
greet("Hello World!")

def greet(message, sender, receiver):
    print(f"To: {receiver} !")
    print(f"Message: {message}")
    print(f"From: {sender}")

greet("Welcome to the team!", "Steven", "John")