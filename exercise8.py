numbers = []  
sum = 0

while True:
    number = int(input("Enter a number (STOP = 0): "))
    if number == 0:
        break
    numbers.append(number)  
    sum += number

if numbers: 
    average = sum / len(numbers)
    minimum = min(numbers)
    print(f"Sum: {sum}, Average: {(average)}, Minimum: {minimum}")
   
else:
    print("No numbers were entered.")