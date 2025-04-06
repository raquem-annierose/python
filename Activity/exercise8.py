numbers = []  
sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    numbers.append(number)  
    sum += number

if numbers: 
    average = sum / len(numbers)
    minimum = min(numbers)
    print(f"Sum: {sum}")
    print(f"Average: {average}")
    print(f"Minimum: {minimum}")
   
else:
    print("No numbers were entered.")