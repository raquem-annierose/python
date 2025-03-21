
print(type("hello")) 
print(type(5))
print(type(5.0))
print(type(True))
print(type(False))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({"name": "John", "age": 30}))
print(type(None))
print(type(print))

# error code
# my_strings = "hello world"
# my_strings[2] = "a"
# print(my_strings)

print(" ")
my_strings = "hello world"
print(my_strings)
print((my_strings[0]))
print(len(my_strings))
# Create a new string with the desired change
my_strings = my_strings[:2] + "a" + my_strings[3:]
print(my_strings)

my_string = 'hi'
print(my_string)

isEven = True

print(10 // 3)

admin_count = 0

role = input("Enter your role: ")
if role == "admin":
    print("Hello Admin!")
    admin_count += 1
else:
    print("Hello User!")

print(f"There is {admin_count} admin(S) in the system.")

x = 5
y = "5"
print (x * y)

