
sum = 0
while True:
    enter_number = int(input("Please enter a number: "))
    sum += enter_number
    if enter_number == 0:
        break
    
print(f"Sum: {sum}")