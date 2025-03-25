import os
os.system('cls')

list = []
occurence = 5

number = 0
for number in range(occurence):
    list.append(int(input(f"Enter number {number + 1} value: ")))
    number += 1
    
print(list)

def sum_list ():
    number_1 = list[0]
    number_2 = list[1]
    number_3 = list[2]
    number_4 = list[3]
    number_5 = list[4]
    
    total_sum = number_1 + number_2 + number_3 + number_4 + number_5
    print(f"Total Sum: {total_sum}")

def average_list ():
    number_1 = list[0]
    number_2 = list[1]
    number_3 = list[2]
    number_4 = list[3]
    number_5 = list[4]
    
    total_sum = number_1 + number_2 + number_3 + number_4 + number_5
    average = total_sum / 5
    print(f"Average: {average}")

def highest_list ():
    number_1 = list[0]
    number_2 = list[1]
    number_3 = list[2]
    number_4 = list[3]
    number_5 = list[4]

    highest_num = max(number_1, number_2, number_3, number_4, number_5)
    print(f"Highest Number: {highest_num}")

def factorial_calculator():
    num = int(input("Enter a number: "))
    fact = 1
    for number in range(1, num + 1):
        fact *= number
    print(f"Factorial: {fact}")



sum_list()
average_list()
highest_list()
factorial_calculator()

